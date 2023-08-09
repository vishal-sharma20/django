from django.contrib import admin
from django.urls import path
from second_app import views as main_views

urlpatterns = [
    path('',main_views.main,name='home'),
    path('day/<day>/',main_views.day,name='xyz'),
    
]
