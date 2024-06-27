
from django.urls import path,include
from app import views
from .views import register

urlpatterns = [
    
    # path('home/',views.home),
    path('register/',views.register),
]