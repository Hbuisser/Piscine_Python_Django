from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
    path('logout', views.logout, name='logout')
    # path('login/', views.login, name='login'),
    # path('', views.usercreation, name='index'),
]
