from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index, name="index"),
    path('index.html',views.index),
    path('aleatory.html', views.random),
    path('NEXT.html', views.next, name="next"),
    path('BACK.html', views.next, name="back"),
    path('aleatorio', views.random, name="random"),
]