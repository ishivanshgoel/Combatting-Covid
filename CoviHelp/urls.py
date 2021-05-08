from django.urls import path

from . import views
from . import login
from . import register

urlpatterns = [
    path('', views.index, name='index'),

    
    path('oxygen', views.oxygen, name="oxygen"),
    path('hospitals', views.hospitals, name='hospitals'),
    path('pharma', views.pharma, name='pharma'),
    path('plasma', views.plasma, name='plasma'),

    path('login', login.loginview, name='login'),

    path('user', login.user, name="user"),
    path('user/plasma', login.plasma, name="userplasma"),
    path('user/oxygen', login.oxygen, name="useroxygen"),
    
    path('user/pharma', login.pharma, name="userpharma"),
    path('user/hospital', login.hospital, name="userhospital"),

    path('register', register.register, name='register'),

    path('helper/districts/', login.getDistricts, name='getdistricts')
]
