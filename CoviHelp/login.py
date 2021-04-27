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
            return HttpResponseRedirect('/user')
        else:
            return HttpResponse('Invalid username/ password')

    else:
        return HttpResponseRedirect("/")

## user view - display after login

@login_required
def user(request):
    '''
    user
    '''
    print(request.user)
    return render(request, "user/account.html")

@login_required
def plasma(request):
    '''
    user
    '''
    print(request.user)
    return render(request, "user/plasma.html")

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


