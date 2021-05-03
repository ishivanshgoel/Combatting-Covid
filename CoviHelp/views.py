from django.shortcuts import render
from django.http import HttpResponse

from .models import Oxygen, Pharma, Plasma, Hospital

# Create your views here.
def index(request):
    return render(request, "public/index.html")
    
def oxygen(request):
    st = Statesdata()
    states = st.getStates()
    return render(request, "public/oxygen.html", {'states': states})


def hospitals(request):
    return render(request, "public/hospitals.html")

def pharma(request):
    st = Statesdata()
    states = st.getStates()
    return render(request, "public/pharma.html", {'states': states})
