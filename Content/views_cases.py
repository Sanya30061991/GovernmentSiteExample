from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import Citizen, Project, ProjectPhoto, Vote


def get_data_context_transfer(request):
    """This method creates context for the profile page
     when you look at someone else's profile"""
    prof_id = request.GET['id']
    context = {
        'cit':Citizen.objects.get(id=prof_id),
        'user':User.objects.get(id=prof_id)
    }
    return context

def context_data_preparing(request):
    """Prepares context data for rendering in html page."""
    try:
        context = {
            'cit':Citizen.objects.get(id=request.user.id),
            'user':request.user
        }
    except Exception:
        context = {
            'cit':None,
            'user':None
        }
    return context

def log_off(request):
    """Simple logging-in method."""
    logout(request)
    return redirect("start")

def auth(request, context):
    """Authentication method, which consists of login and authenticate methods."""
    email=request.POST['email']
    password=request.POST['password']
    user = authenticate(username=email, password=password)
    if user is not None:
        login(request, user)
        return redirect("main")
    else:
        context['errors'] = "Invalid login or password!"
        return render(request, 'Content/login.html', context)


def login_check(request):
    """Method that checks whether user is logged in or not. Returns also a Citizen object if user is logged in."""
    context = {
        'user':None,
        'cit':None
    }
    if request.user.is_authenticated:
        context = {
            'user':request.user,
            'cit':Citizen.objects.get(id=request.user.id)
        }
    return context

def handle_image(request, context):
    """Function that takes  image out of request.FILES and cuts off it's prefix and common name."""
    postfix = request.FILES['avatar'].name[request.FILES['avatar'].name.rfind("."):]
    title = request.user.email
    request.FILES['avatar'].name = request.user.email+postfix
    context['cit'].avatar = request.FILES['avatar']
    context['cit'].save()

def user_creating(request, context):
    """Registration method, which considers user's job and status, and saves models."""
    deps = {
            '01':'Presidential branch',
            '02':'Healthcare Sphere',
            '03':'Educational Sphere',
            '04':'Military Sphere',
            '05':'Official'
        }
    ranks = {
            '01':'Ordinary worker',
            '02':'Manager',
            '03':'Secretary',
            '04':'Cleaner',
            '05':'Overseer',
            '06':'Main'
        }
    date_source = request.POST['birth_day']
    date = date_source[-4:] + "-" + date_source[-7:-5] + "-" + date_source[-10:-8]
    User.objects.create_user(
        username = request.POST['email'],
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = request.POST['password'],
    )
    new = Citizen(
        user = User.objects.get(username = request.POST['email']),
        department = deps.get(request.POST['res_code'][:2], "Other"),
        rank = ranks.get(request.POST['res_code'][2:4], "Citizen"),
        birth_day = date,
        gender = request.POST['gender'],
    )
    if new.rank != "Citizen":
        new.is_staff = True
    new.save()
    return redirect("login")

def project_creating(request):
    """
    New project creationg functions. Creates project model,
    updates Citizen model, saves uploaded files to media.
    """
    citizen_id = request.user.id
    citizen = Citizen.objects.get(id=citizen_id)
    project = Project(
        title = request.POST['title'],
        desc = request.POST['desc'],
        votes = 0,
        creator = citizen,
        sphere = request.POST['sphere']
    )
    citizen.__dict__[request.POST['sphere'].lower()+'_projects'] += 1
    citizen.save()
    project.save()
    k = 1
    dest = "project_photos"
    for file in request.FILES.getlist('images'):
        postfix = file.name[file.name.rfind("."):]
        title = citizen.user.first_name + \
                "_" + citizen.user.last_name + \
                "_" + project.title + \
                "_" + str(k) + postfix
        file.name = title 
        photo = ProjectPhoto(
            title = title,
            project = project,
            photo = file
        )
        photo.save()
        k += 1
    return redirect("project_finished")
    

def vote_for_project(request):
    """This method creates new vote of the official for the project."""
    project = Project.objects.get(id=request.POST['id'])
    votes = Vote.objects.filter(
        project = project,
        voter = Citizen.objects.get(user=request.user.id)
    )
    if len(votes) == 0:
        vote = Vote(
            project = project,
            voter = Citizen.objects.get(user=request.user.id)
        )
        vote.save()
        project.votes += 1
        project.save()

def project_view_context_data_preparation(request):
    proj_id = request.GET['id']
    context = {
        'project':Project.objects.get(id=proj_id),
        'photos':ProjectPhoto.objects.filter(project = proj_id)
    }
    context['vote'] = Vote.objects.filter(
        project_id=proj_id,
        voter_id=request.user.id
        )
    if len(context['vote']) > 0:
        context['vote'] = context['vote'][0]
    else:
        context['vote'] = None
    return context