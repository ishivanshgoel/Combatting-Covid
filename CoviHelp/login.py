from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# user info model
from .models import UserInfo
from .models import Plasma, Oxygen, Pharma

# helper functions
from .Helpers.Statesdata import Statesdata
import json

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
            return redirect(user)
        else:
            return HttpResponse('Invalid username/ password')

    else:
        return HttpResponse("Not Allowed")

# user view - display after login


@login_required
def user(request):
    '''
    user
    '''
    return render(request, "user/account.html")


@login_required
def plasma(request):
    '''
    user
    '''
    if request.method == 'POST':
        try:
            plasma = Plasma()
            plasma.user = request.user
            plasma.name = request.POST['name']
            plasma.state = request.POST['state']
            plasma.city = request.POST['city']
            plasma.donortype = request.POST['donortype']
            plasma.contact = request.POST['contact']
            plasma.save()
            return HttpResponse('Saved')
        except:
            return HttpResponse('Error')
    else:
        st = Statesdata()
        states = st.getStates()
        return render(request, "user/plasma.html", {
            'states': states
        })


@login_required
def oxygen(request):
    '''
    user
    '''
    if request.method == 'POST':
        try:
            Oxy = Oxygen()
            Oxy.user = request.user
            Oxy.name = request.POST['name']
            Oxy.state = request.POST['state']
            Oxy.city = request.POST['city']
            Oxy.contact = request.POST['contact']
            Oxy.address = request.POST['address']
            Oxy.save()
            return HttpResponse('Saved')
        except:
            return HttpResponse('Error')
    else:
        st = Statesdata()
        states = st.getStates()
        return render(request, "user/oxygen.html", {
            'states': states
        })


@login_required
def hospital(request):
    '''
    user
    '''
    print(request.user)
    return render(request, "user/hospital.html")


@login_required
def pharma(request):
    '''
    user
    '''
    available_drugs = ["Tocilizumab", "Remdesivir",
                       "Favipiravir", "Fabiflu 200 MG"]
    if request.method == 'POST':
        try:
            pharma = Pharma()
            pharma.user = request.user
            pharma.name = request.POST['name']
            pharma.state = request.POST['state']
            pharma.city = request.POST['city']
            pharma.contact = request.POST['contact']
            pharma.address = request.POST['address']
            pharma.available_drugs=request.POST['drugs']
            pharma.save()
            return HttpResponse('Saved')
        except:
            return HttpResponse('Error')
    else:
        st = Statesdata()
        states = st.getStates()
        return render(request, "user/pharma.html", {
            'states': states,
            "drugs":available_drugs
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
