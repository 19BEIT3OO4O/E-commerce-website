from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='home'),
    path('services/',views.services, name='services'),
    path('Contact us/',views.index, name='index'),
    path('login/',views.inbox, name='inbox')
    
    
]