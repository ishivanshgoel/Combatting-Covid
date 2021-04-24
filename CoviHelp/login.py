from django.shortcuts import render
from django.http import HttpResponse

from .forms import OxygenUser, HospitalUser, PharmaUser

## all login views
def oxygenlogin(request):
    if request.method == 'POST':
        pass
    else:
        form=OxygenUser()
        return render(request, "public/login/oxygen.html", {'form':form})

def hospitalslogin(request):
    if request.method == 'POST':
        pass
    else:
        form=HospitalUser()
        return render(request, "public/login/hospitals.html", {'form':form})

def pharmalogin(request):
    if request.method == 'POST':
        pass
    else:
        form=PharmaUser()
        return render(request, "public/login/pharma.html", {'form':form})