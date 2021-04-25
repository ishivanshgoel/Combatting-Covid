from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate

# user info model
from .models import UserInfo

## all login views

def login(request):
    '''
    if request is POST then verify the credentials of the user and redirect to their respective location based on their user type
    else redirect to '/'
    '''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = authenticate(username=email, password=password)
        except:
            return HttpResponse('Some Error Occured')
        if user is not None:
            userInfo = UserInfo.objects.get(user__username=user)
            print(userInfo)
            print("User type", userInfo.user_type)
            if(userInfo.user_type == 'O'):
                return HttpResponseRedirect('/user/oxygen')
            elif(userInfo.user_type == 'P'):
                return HttpResponseRedirect('/user/pharma')
            elif(userInfo.user_type == 'H'):
                return HttpResponseRedirect('/user/hospital')
            elif(userInfo.user_type == 'B'):
                return HttpResponseRedirect('/user/plasma')
        else:
            return HttpResponse('Invalid username/ password')

    else:
        return HttpResponseRedirect("/")

## user views - display after login

@login_required
def oxygenuser(request):
    '''
    if the user is oxygen supplier
    '''
    
    return HttpResponse('I am Oxygen Supplier')

@login_required
def hospitaluser(request):
    '''
    if the user is hospital
    '''
    return HttpResponse('I am a Hospital')

@login_required
def pharmauser(request):
    '''
    if the user is medicine supplier
    '''
    return HttpResponse('I am Medicine Supplier')

@login_required
def plasmauser(request):
    '''
    if the user is plasma donner
    '''
    return HttpResponse('I am Plasma Donor')


