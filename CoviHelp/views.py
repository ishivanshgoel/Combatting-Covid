from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Oxygen, Pharma, Plasma, Hospital, Report, Feedback

from .Helpers.Statesdata import Statesdata
from .Helpers.Utilities import Utilities

st = Statesdata()
ut = Utilities()

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
        states = st.getStates()
        return render(request, "public/pharma.html", {'states': states})

def hospitals(request):
    try:
        state = request.GET.getlist('state')[0]
        city = request.GET.getlist('city')[0]
        resources=Hospital.objects.filter(state=state,city=city)
        beds=[]
        for b in resources:
            bed=b.bedsavailable.strip("[]").split(",")
            beds.append(bed)
        return render(request, "public/hospitalView.html", {
            "cleaned_resources": zip(resources, beds)
        })
    except:
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
        states = st.getStates()
        return render(request, "public/plasma.html", {'states': states})

def report(request, id):
    if request.method == 'POST':
        try:
            r = Report()
            r.comments = request.POST['comments']
            r.id = ut.gen_id('user-name', r.comments[0], 'state', 'report','contact')
            modelType = request.POST['ModelType']
            if modelType == "Oxygen":
                r.item = Oxygen.objects.get(id=id)
            elif modelType == "Pharma":
                r.item = Pharma.objects.get(id=id)
            elif modelType == "Plasma":
                r.item = Plasma.objects.get(id=id)
            r.save()
            messages.success(request, 'Comment Submitted!')
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            messages.warning(request, 'Error!!')
            return render(request, "public/index.html")
    else:
        messages.warning(request, 'Method Not Allowed!')
        return render(request, "public/index.html")

def feedback(request):
    if request.method == 'POST':
        try:
            f = Feedback()
            f.contact = request.POST['contact']
            f.message = request.POST['message']
            f.id = ut.gen_id('user-name', f.message[0], 'state', 'feedback','contact')
            f.save()
            messages.success(request, 'Message Submitted!')
            return redirect(request.META.get('HTTP_REFERER'))
        except:
            messages.warning(request, 'Error!!')
            return render(request, "public/index.html")
    else:
        messages.warning(request, 'Method Not Allowed!')
        return render(request, "public/index.html")
