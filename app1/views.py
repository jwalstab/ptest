from django.shortcuts import render
from django.http import HttpResponse
from app1.models import glob

def home(request):
    return render (request, 'home.html',{'name': 'Jay' })

def add(request):
    print(request)
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    val3 = val1 + val2
    newGlob = glob()
    newGlob.name = "ralph"
    newGlob.level = val3
    return render(request, 'result.html',{
        'result': str(val3),
        'globber' : newGlob
        })