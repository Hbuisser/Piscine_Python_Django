from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_view, name='form'),
    path('ex02', views.create_view, name='form')
]