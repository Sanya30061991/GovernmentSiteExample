from django.shortcuts import render, redirect
from .models import Citizen, ProjectPhoto, Project
from .forms import CitReg, UserReg, UserLog, AvatarUpload

# Create your views here.
from .views_cases import auth, login_check, handle_image, \
                        log_off, user_creating, \
                        project_creating, context_data_preparing, \
                        get_data_context_transfer

def team(request):
    context = context_data_preparing(request)
    context['team'] = Citizen.objects.all()
    return render(request, 'Content/team.html', context)

def project_make(request):
    context = login_check(request)
    if request.method == "POST":
        return project_creating(request)
    return render(request, 'Content/create_project.html', context)

def log_ex(request):
    return log_off(request)
    
def logon(request):
    context = {
        'form':UserLog(),
        'errors':""
    }
    if request.method == "POST":
        return auth(request, context)
    return render(request, 'Content/login.html', context)

def start(request):
    context = login_check(request)
    return render(request, 'Content/start.html', context)

def main(request):
    context = login_check(request)
    try:
        project = Project.objects.latest('id')
        context['project'] = project
        context['photos'] = ProjectPhoto.objects.filter(project=project.id)
    except Exception:
        context['project'] = None
    return render(request, 'Content/main.html', context)

def profile(request):
    context = login_check(request)
    if request.method == 'POST':
        handle_image(request, context)
    elif request.method == "GET" and 'id' in request.GET:
        context = get_data_context_transfer(request)
    context['form'] = AvatarUpload()
    return render(request, 'Content/profile.html', context)

def reg(request):
    context = {
        'form1':CitReg(),
        'form2':UserReg()
    }
    if request.method == "POST":
        return user_creating(request, context)
    return render(request, 'Content/registration.html', context)

def finished_project(request):
    return render(request, 'Content/finished_project.html')