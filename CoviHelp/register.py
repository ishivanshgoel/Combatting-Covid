from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# default User Model
from django.contrib.auth.models import User

# Other Models
from .models import UserInfo

# register view
def register(request):
    '''
    process the form and 
    register the user
    '''
    if request.method == 'POST':
        userType = request.POST.get('userType', None)
        userPassword = request.POST.get('userPassword', None)
        userEmail = request.POST.get('userEmail', None)

        if userType and userPassword and userEmail:
            user = None
            try:
                user = User.objects.get(username=userEmail)
            except User.DoesNotExist:
                user = None

            if user is None:
                user = User.objects.create_user(username = userEmail, password = userPassword)
                userInfo = UserInfo()
                userInfo.user = user
                userInfo.user_type = userType
                userInfo.save()
                return HttpResponse('User Created')
            else:
                return HttpResponse('User already exists')
        else:
            return HttpResponse('Bad Request')
    else:
        return HttpResponseRedirect("/")