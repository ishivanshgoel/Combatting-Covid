from django.urls import path
from django.conf.urls import url

from . import views
from . import login
from . import register

urlpatterns = [
    path('', views.index, name='index'),

    
    path('oxygen', views.oxygen, name="oxygen"),
    path('hospital', views.hospitals, name='hospital'),
    path('pharma', views.pharma, name='pharma'),
    path('plasma', views.plasma, name='plasma'),

    path('login', login.loginview, name='login'),

    path('user', login.user, name="user"),
    path('user/plasma', login.plasma, name="userplasma"),
    path('user/oxygen', login.oxygen, name="useroxygen"),
    path('user/pharma', login.pharma, name="userpharma"),
    path('user/hospital', login.hospital, name="userhospital"),

    path('user/completelist',login.completelist, name="usercompletelist"),

    path('user/modify/<str:id>',login.modify,name='usermodify'),

    path('register', register.register, name='register'),

    path('report/<str:id>',views.report, name="report"),
    path('feedback', views.feedback, name="feedback"),

    path('helper/districts/', login.getDistricts, name='getdistricts')
]
