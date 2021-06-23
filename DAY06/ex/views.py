from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from .models import *
from .forms import *
from django.conf import settings
import random
from django.shortcuts import render, redirect

# https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

def home(request):
    form = TipForm(request.POST or None)
    tips = []
    if form.is_valid():
        form = TipForm()
        tip = Tip(author=request.user, content=request.POST.dict().get('content'))
        tip.save()
        tips = Tip.objects.all()
    if 'name' in request.COOKIES:
        user = request.COOKIES['name']
        tips = Tip.objects.all()
        response = render(request, 'base.html', {'usr_name': user, 'form': form, 'tip': tips})
    else:
        user = random.choice(settings.USER_NAMES)
        request.COOKIES['name'] = user
        tips = Tip.objects.all()
        response = render(request, 'base.html', {'usr_name': user, 'form': form, 'tip': tips})
        response.set_cookie('name', user, max_age=settings.COOKIES_TIME)
    return response

def register(request):
    if  request.user.is_authenticated:
        return redirect('home')
    if  request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            new_user.save()
            auth.login(request, new_user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')


# film = []
#     try:
#         movies =  Movies.objects.all()
#         for movie in movies:
#             film.append((movie.title, movie.episode_nb, movie.opening_crawl, movie.director, movie.producer, movie.release_date ))
#     except psycopg2.DatabaseError as e:
#         return HttpResponse(e)
#     if film == []:
#         return HttpResponse("No data available")
#     else:
#         return render(request, "ex05/display.html", {'film': film})
