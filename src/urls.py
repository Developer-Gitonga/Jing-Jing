from django.urls import path
from .views import *
from . import views
from django.contrib.auth import views as view

urlpatterns = [
    path('', views.Home, name='home'),
    path('cart/', views.Cart, name='cart'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', view.LogoutView.as_view(next_page='login'), name='logout'),
]