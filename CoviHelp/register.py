from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime

# default User Model
from django.contrib.auth.models import User

# Other Models
from .models import UserInfo

# Helpers
from .Helpers.Utilities import Utilities
ut = Utilities()

# register view
def register(request):
    '''
    process the form and 
    register the user
    '''
    if request.method == 'POST':
        userPassword = request.POST.get('userPassword', None)
        userEmail = request.POST.get('userEmail', None)

        if userPassword and userEmail:
            user = None
            try:
                user = User.objects.get(username=userEmail)
            except User.DoesNotExist:
                user = None

            if user is None:
                user = User.objects.create_user(username = userEmail, password = userPassword)
                userInfo = UserInfo()
                userInfo.user = user
                userInfo.id = ut.gen_id('user', 'user-name', 'user-type', 'register', 'user-contact')
                userInfo.save()
                messages.success(request, 'Registered Successfully!! Headover to Login...')
                return render(request, "public/index.html")
            else:
                messages.warning(request, 'User already exists!! Headover to Login...')
                return render(request, "public/index.html")
        else:
            messages.error(request, 'Bad Request')
            return render(request, "public/index.html")
    else:
        return HttpResponseRedirect("/")