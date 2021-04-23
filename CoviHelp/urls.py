from django.urls import path

from . import views
from . import login
from . import register

urlpatterns = [
    path('', views.index, name='index'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('pharma', views.pharma, name='pharma'),

    path('oxygenlogin', login.oxygenlogin, name='oxygenlogin'),
    path('hospitalslogin', login.hospitalslogin, name='hospitalslogin'),
    path('pharmalogin', login.pharmalogin, name='pharmalogin'),

    path('oxygenregister', register.oxygenregister, name='oxygenregister'),
    path('hospitalsregister', register.hospitalsregister, name='hospitalsregister'),
    path('pharmaregister', register.pharmaregister, name='pharmaregister'),
]