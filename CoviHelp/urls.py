from django.urls import path

from . import views
from . import login
from . import register

urlpatterns = [
    path('', views.index, name='index'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('pharma', views.pharma, name='pharma'),

    path('login', login.login, name='login'),
    path('user/oxygen', login.oxygenuser, name="oxygenuser"),
    path('user/plasma', login.plasmauser, name="plasmauser"),
    path('user/hospital', login.hospitaluser, name="hospitaluser"),
    path('user/pharma', login.oxygenuser, name="oxygenuser"),

    path('register', register.register, name='register'),
]