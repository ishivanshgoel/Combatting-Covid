from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

# user info model
from .models import UserInfo
from .models import Plasma

# helper functions
from .Helpers.Statesdata import Statesdata
import json

## all login views
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

## user view - display after login

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
    print(request.user)
    return render(request, "user/oxygen.html")

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
    print(request.user)
    return render(request, "user/pharma.html")



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

