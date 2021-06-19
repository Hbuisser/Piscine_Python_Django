"""d04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from ex02.views import create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('ex01/', base),
    # path('ex01/django', django_view),
    # path('ex01/display', display_view),
    # path('ex01/templates', templates_view),
    path('ex02/', create_view),
    path('', RedirectView.as_view(url='ex02/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
