from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    ## page showing navigating options
    return render(request, "public/index.html")
    
def oxygen(request):
    return render(request, "public/oxygen.html")

def hospitals(request):
    return render(request, "public/hospitals.html")

def pharma(request):
    return render(request, "public/pharma.html")