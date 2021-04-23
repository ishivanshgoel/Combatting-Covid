from django.shortcuts import render
from django.http import HttpResponse

## all login views

def oxygenlogin(request):
    return render(request, "public/login/oxygen.html")

def hospitalslogin(request):
    return render(request, "public/login/hospitals.html")

def pharmalogin(request):
    return render(request, "public/login/pharma.html")