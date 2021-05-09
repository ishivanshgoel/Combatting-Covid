from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Oxygen, Pharma, Plasma, Hospital, Report

from .Helpers.Statesdata import Statesdata
import json

# Create your views here.
def index(request):
    return render(request, "public/index.html")

### send state and district wise
def oxygen(request):
    try:
        state = request.GET.getlist('state')[0]
        city = request.GET.getlist('city')[0]
        resources=Oxygen.objects.filter(state=state,city=city)
        return render(request, "public/oxygenView.html", {
            "resources":resources
        })
    except:
        st = Statesdata()
        states = st.getStates()
        return render(request, "public/oxygen.html", {'states': states})

def pharma(request):
    try:
        state = request.GET.getlist('state')[0]
        city = request.GET.getlist('city')[0]
        resources=Pharma.objects.filter(state=state,city=city)
        drugs=[]
        for med in resources:
            med=med.available_drugs.strip("[]").split(",")
            drugs.append(med)
        return render(request, "public/pharmaView.html", {
            "cleaned_resources": zip(resources, drugs)
        })
    except:
        st = Statesdata()
        states = st.getStates()
        return render(request, "public/pharma.html", {'states': states})

def hospitals(request):
    try:
        state = request.GET.getlist('state')[0]
        city = request.GET.getlist('city')[0]
        resources=Hospital.objects.filter(state=state,city=city)
        return render(request, "public/oxygenView.html", {
            "resources":resources
        })
    except:
        st = Statesdata()
        states = st.getStates()
        return render(request, "public/hospitals.html", {'states': states})

def plasma(request):
    try:
        state = request.GET.getlist('state')[0]
        city = request.GET.getlist('city')[0]
        resources=Plasma.objects.filter(state=state,city=city)
        return render(request, "public/plasmaView.html", {
            "resources":resources
        })
    except:
        st = Statesdata()
        states = st.getStates()
        return render(request, "public/plasma.html", {'states': states})

def report(request, id):
    comments = request.POST['comments']
    modelType = request.POST['ModelType']
    if modelType == "Oxygen":
        print(Oxygen.objects.get(id=id))
    elif modelType == "Pharma":
        print(Pharma.objects.get(id=id))
    elif modelType == "Plasma":
        print(Plasma.objects.get(id=id))
    return HttpResponse("working")