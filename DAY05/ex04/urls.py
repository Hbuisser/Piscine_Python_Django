from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.create_table, name='index'),
    path('populate/', views.populate, name='index'),
    path('display/', views.display, name='index'),
    path('remove/', views.remove, name='index'),
]