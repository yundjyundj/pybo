from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('menu1.html', views.menu1),
    
]