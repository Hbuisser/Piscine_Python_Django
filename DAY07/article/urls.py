from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from . import views
from article.views import ArticleListView, PublicationView, DetailView, FavouritesView
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='Articles/')),
    path('Articles/', ArticleListView.as_view(), name='article-list'),
    path('login/', auth_views.LoginView.as_view(template_name='article/contact.html', redirect_authenticated_user = True), name='contact'),
    path('publications/', PublicationView.as_view(), name='publications'),
    path('detail/<slug:pk>/', DetailView.as_view(), name='article-detail'),
    path('logout/', auth_views.LogoutView.as_view(template_name='article/logout.html'), name='logout'),
    path('favourites/', FavouritesView.as_view(), name='favourites')
]


# class based view are looking for templates with those names:
# <app>/<model>_<viewtype>.html
