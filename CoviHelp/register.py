from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# default User Model
from .models import User

# all register views

## register
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
                user = User.objects.get(email=userEmail)
            except User.DoesNotExist:
                user = None

            if user is None:
                user = User()
                user.email = userEmail
                user.password = userPassword
                user.user_type = userType
                user.save()
                return HttpResponse('User Created')
            else:
                return HttpResponse('User already exists')
        else:
            return HttpResponse('Bad Request')
    else:
        return HttpResponseRedirect("/")