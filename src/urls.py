from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('cart/', views.Cart, name='cart'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout, name='logout'),
]