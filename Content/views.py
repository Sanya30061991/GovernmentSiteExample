from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import login, authenticate, logout
from .models import Citizen
from .forms import CitReg, UserReg, UserLog, AvatarUpload

# Create your views here.

def log_ex(request):
    logout(request)
    return redirect("start")

def logon(request):
    context = {
        'form':UserLog(),
        'errors':""
    }
    if request.method == "POST":
        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            context['errors'] = "Invalid login or password!"
    return render(request, 'Content/login.html', context)

def start(request):
    a = 1/0
    if request.user.is_authenticated:
        context = {
            'user':request.user
        }
    return render(request, 'Content/start.html', context)


def main(request):
    context = {
        'user':None
    }
    if request.user.is_authenticated:
        context = {
            'user':request.user
        }
    return render(request, 'Content/main.html', context)

def handle_uploaded_file(file, request):
    with open(f'media/avatars/{request.user.email}.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def profile(request):
    context = {
        'user':None
    }
    if request.user.is_authenticated:
        context = {
            'cit':Citizen.objects.get(id=request.user.id),
            'form':AvatarUpload(),
            'test':5
        }
    if request.method == 'POST':
        postfix = request.FILES['avatar'].name[request.FILES['avatar'].name.rfind("."):]
        request.FILES['avatar'].name = request.user.email+postfix
        handle_uploaded_file(request.FILES['avatar'], request)
        context['cit'].avatar = request.FILES['avatar']
        context['cit'].save()
    return render(request, 'Content/profile.html', context)

def reg(request):
    context = {
        'form1':CitReg(),
        'form2':UserReg()
    }
    if request.method == "POST":
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
        new.save()
        return redirect("login")
    return render(request, 'Content/registration.html', context)