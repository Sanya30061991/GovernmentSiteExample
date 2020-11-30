from django.shortcuts import render

# Create your views here.


def start_2(request):
    return render(request, 'Content/start2.html')

def start_3(request):
    return render(request, 'Content/start3.html')

def start(request):
    return render(request, 'Content/start.html')

def reg(request):
    return render(request, 'Content/registration.html')