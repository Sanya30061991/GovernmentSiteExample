from django.shortcuts import render

from .models import Citizen
from .forms import CitReg
# Create your views here.


def start_2(request):
    return render(request, 'Content/start2.html')

def start_3(request):
    return render(request, 'Content/start3.html')

def start(request):
    return render(request, 'Content/start.html')

def reg(request):
    context = {
        'form':CitReg()
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
        new = Citizen(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            department = deps.get(request.POST['res_code'][:2], "Other"),
            rank = ranks.get(request.POST['res_code'][2:4], "Citizen"),
            birth_day = date,
            gender = request.POST['gender'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
        new.save()
    return render(request, 'Content/registration.html', context)