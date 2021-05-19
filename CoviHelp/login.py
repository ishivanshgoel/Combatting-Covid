from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# user info model
from .models import UserInfo
from .models import Plasma, Oxygen, Pharma, Hospital

# helper functions
from .Helpers.Statesdata import Statesdata
from .Helpers.Utilities import Utilities
from .Helpers.Data import Data
import json
import datetime

# helpers
dt = Data()
available_drugs = dt.available_drugs() 
bed_options = dt.bed_options()
    
st = Statesdata()
states = st.getStates()
ut = Utilities()


# all login views
def loginview(request):
    '''
    if request is POST then verify the credentials of the user and redirect to their respective location based on their user type
    else redirect to '/'
    '''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            u = authenticate(request, username=email, password=password)
        except:
            return HttpResponse('Some Error Occured')
        if u is not None:
            login(request, u)
            return redirect(oxygen)
        else:
            messages.warning(request, 'Invalid username/ password')
            return render(request, "public/index.html")
    else:
        messages.warning(request, 'Not Allowed')
        return render(request, "public/index.html")

# user view - display after login
@login_required
def user(request):
    '''
    user
    '''
    return render(request, "user/oxygen.html")


@login_required
def plasma(request):
    global states
    plasma = Plasma.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            p = Plasma()
            p.user = request.user
            p.name = request.POST['name']
            p.state = request.POST['state']
            p.city = request.POST['city']
            p.donortype = request.POST['donortype']
            p.contact = request.POST['contact']
            p.blood_group = request.POST['bloodgroup']
            p.id = ut.gen_id(p.user, p.name, p.state, 'plasma', p.contact)
            p.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.warning(request, 'Error!!')
        return render(request, "user/plasma.html", {
            'states': states,
            "plasma" : plasma
        })
    else:
        return render(request, "user/plasma.html", {
            'states': states,
            "plasma" : plasma
        })


@login_required
def oxygen(request):
    global states
    oxygen = Oxygen.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            Oxy = Oxygen()
            Oxy.user = request.user
            Oxy.name = request.POST['name']
            Oxy.state = request.POST['state']
            Oxy.city = request.POST['city']
            Oxy.contact = request.POST['contact']
            Oxy.address = request.POST['address']
            Oxy.id = ut.gen_id(Oxy.user, Oxy.name, Oxy.state, 'oxygen', Oxy.contact)
            Oxy.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')
        return render(request, "user/oxygen.html", {
            'states': states,
            'oxygen' : oxygen
        })

    else:
        return render(request, "user/oxygen.html", {
            'states': states,
            'oxygen' : oxygen
        })


@login_required
def hospital(request):
    '''
    user
    '''
    global states
    hospitals = Hospital.objects.filter(user=request.user)
    if request.method == 'POST':
        try:
            H = Hospital()
            H.user = request.user
            H.name = request.POST['name']
            H.state = request.POST['state']
            H.city = request.POST['city']
            H.contact = request.POST['contact']
            H.address = request.POST['address']
            H.bedsavailable = request.POST.getlist('checks[]')
            H.id = ut.gen_id(H.user, H.name, H.state, 'hospital', H.contact)
            print(H)
            H.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')
        return render(request, "user/hospital.html", {
            "states": states,
            "beds": bed_options,
            'hospitals' : hospitals
        })

    else:
        return render(request, "user/hospital.html", {
            "states": states,
            "beds": bed_options,
            'hospitals' : hospitals
        })

@login_required
def pharma(request):
    global available_drugs, states
    pharma = Pharma.objects.filter(user=request.user)

    if request.method == 'POST':
        try:
            p = Pharma()
            p.user = request.user
            p.name = request.POST['name']
            p.state = request.POST['state']
            p.city = request.POST['city']
            p.contact = request.POST['contact']
            p.address = request.POST['address']
            p.available_drugs = request.POST.getlist('checks[]')
            p.id = ut.gen_id(p.user, p.name, p.state, 'pharma', p.contact)
            p.save()
            messages.success(request, 'Thankyou for sharing the information.')
        except:
            messages.error(request, 'Error!!')

        return render(request, "user/pharma.html", {
            "states": states,
            "drugs":available_drugs,
            "pharma":pharma
        })
    else:
        print(available_drugs)
        return render(request, "user/pharma.html", {
            "states": states,
            "drugs":available_drugs,
            "pharma":pharma
        })


### Helper Routes ###
def getDistricts(request):
    '''
    get all districts
    '''
    try:
        state = request.GET.getlist('state')[0]
        st = Statesdata()
        data = st.getDistricts(state)
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')
    except:
        return HttpResponse('Error')
