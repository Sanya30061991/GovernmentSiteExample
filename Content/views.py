from django.shortcuts import render, redirect
from .models import Citizen
from .forms import CitReg, UserReg, UserLog, AvatarUpload

# Create your views here.
from .views_cases import auth, login_check, handle_image, log_off


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
    return render(request, 'Content/main.html', context)

def profile(request):
    context = login_check(request)
    context = {
        'cit':Citizen.objects.get(id=request.user.id),
        'form':AvatarUpload(),
        'test':5
    }
    if request.method == 'POST':
        handle_image(request, context)
    return render(request, 'Content/profile.html', context)

def reg(request):
    context = {
        'form1':CitReg(),
        'form2':UserReg()
    }
    if request.method == "POST":
        return user_creating(request, context)
    return render(request, 'Content/registration.html', context)