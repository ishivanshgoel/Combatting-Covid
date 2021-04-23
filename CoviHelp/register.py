from django.shortcuts import render
from django.http import HttpResponse

# all register views

## register
def oxygenregister(request):
    return render(request, "public/register/oxygen.html")

def hospitalsregister(request):
    return render(request, "public/register/hospitals.html")

def pharmaregister(request):
    return render(request, "public/register/pharma.html")