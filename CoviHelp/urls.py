from django.urls import path

from . import views
from . import login
from . import register

urlpatterns = [
    path('', views.index, name='index'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('pharma', views.pharma, name='pharma'),

    path('login/oxygen', login.oxygenlogin, name='oxygenlogin'),
    path('login/hospitals', login.hospitalslogin, name='hospitalslogin'),
    path('login/pharma', login.pharmalogin, name='pharmalogin'),

    path('reg/oxygen', register.oxygenregister, name='oxygenregister'),
    path('reg/hospitals', register.hospitalsregister, name='hospitalsregister'),
    path('reg/pharma', register.pharmaregister, name='pharmaregister'),
]