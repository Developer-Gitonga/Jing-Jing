from django.urls import path
from .views import *
from src import views

urlpatterns = [
    path('', views.Home, name='home'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('profile/<int:pk>/update/', views.edit_user, name='edit_profile'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    # path('posts/',  views.Posted , name="posts" ),
    # path('posts/create',  views.create_post , name="create_posts" ),
    # path('result/', views.calculate_cost, name='result'),
]