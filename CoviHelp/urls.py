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
    path('user', login.user, name="user"),

    path('register', register.register, name='register'),
]