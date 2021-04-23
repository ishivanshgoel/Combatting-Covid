from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('oxygen', views.oxygen, name='oxygen'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('pharma', views.pharma, name='pharma'),
]