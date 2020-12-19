from django.contrib import admin
from django.urls import path
from AlarmClock import views
urlpatterns = [
    path('',views.index,name='home'),
    path("stopwatch",views.stopwatch,name='stopwatch'),
    
]