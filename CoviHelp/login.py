from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

## forms
from .forms import OxygenUser, HospitalUser, PharmaUser

## all login views

def login(request):
    '''
    if request is POST then verify the credentials of the user and redirect to their respective location based on their user type
    else redirect to '/'
    '''
    if request.method == 'POST':
        print("Request: Login")
        pass
    else:
        return HttpResponseRedirect("/")

## user views - display after login

@login_required
def oxygenuser(request):
    '''
    if the user is oxygen supplier
    '''
    pass

@login_required
def hospitaluser(request):
    '''
    if the user is hospital
    '''
    pass

@login_required
def pharmauser(request):
    '''
    if the user is medicine supplier
    '''
    pass

@login_required
def plasmadonneruser(request):
    '''
    if the user is plasma donner
    '''
    pass


