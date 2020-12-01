from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Citizen
from .forms import CitReg, UserReg, UserLog
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
        user = authenticate(email=request.POST['email'])
        # user = authenticate(request, email=email)
        if user is not None:
            # login(request, user)
            print("success")
            # return redirect("main")
        else:
            context['errors'] = "Invalid login or password!"
    return render(request, 'Content/login.html', context)

def start_2(request):
    return render(request, 'Content/start2.html')

def start_3(request):
    return render(request, 'Content/start3.html')

def main(request):
    # user = request.user
    # user_info = {
    #     'fname':user.first_name,
    #     'sname':user.last_name,
    # }
    # print(user)
    # context = {
    #     'user':user_info
    # }
    return render(request, 'Content/start.html')

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
            username = str(request.POST['first_name'] + request.POST['last_name']*2),
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        new = Citizen(
            user = User.objects.get(username = request.POST['first_name'] + request.POST['last_name']*2),
            department = deps.get(request.POST['res_code'][:2], "Other"),
            rank = ranks.get(request.POST['res_code'][2:4], "Citizen"),
            birth_day = date,
            gender = request.POST['gender'],
        )
        new.save()
        return redirect("login")
    return render(request, 'Content/registration.html', context)