from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('ex01/django', views.django_view, name='django'),
    path('ex01/display', views.display_view, name='display'),
    path('ex01/templates', views.templates_view, name='templates'),
]