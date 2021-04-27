from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ## page showing navigating options
    return render(request, "public/index.html")
    
def oxygen(request):
    return render(request, "public/oxygen.html")

def hospitals(request):
    return render(request, "public/hospitals.html")

def pharma(request):
    return render(request, "public/pharma.html")


