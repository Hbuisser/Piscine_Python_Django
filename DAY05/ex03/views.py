from django.shortcuts import render
from psycopg2 import connect, extensions, sql
import psycopg2
import sys
from .models import Movies
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden)

def populate(request):
    result = list()
    try:
        mov1 = Movies(episode_nb=1,title='The Phantom Menace', director='George Lucas', producer="Rick McCallum",
                      release_date='1999-05-19')
        mov1.save()
        result.append('Ok')
        mov2 = Movies(episode_nb=2, title='Attack of the Clones', director='George Lucas', producer="Rick McCallum",
                  release_date='2002-05-16')
        mov2.save()
        result.append('Ok')
        mov3 = Movies(episode_nb=3, title='Revenge of the Sith', director='George Lucas', producer="Rick McCallum",
                  release_date='2005-05-19')
        mov3.save()
        result.append('Ok')
        mov4 = Movies(episode_nb=4, title='A New Hope', director='George Lucas', producer="Gary Kurtz, Rick McCallum",
                  release_date='1977-05-25')
        mov4.save()
        result.append('Ok')
        mov5 = Movies(episode_nb=5, title='The Empire Strikes Back', director='George Lucas', producer="Gary Kutz, Rick McCallum",
                  release_date='1980-05-17')
        mov5.save()
        result.append('Ok')
        mov6 = Movies(episode_nb=6, title='Return of the Jedi', director='Richard Marquand', producer="Howard G. Kazanjian, George Lucas, Rick McCallum",
                  release_date='1983-05-25')
        mov6.save()
        result.append('Ok')
        mov7 = Movies(episode_nb=7, title='The Force Awakens', director='J. J. Abrams', producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk",
                  release_date='2015-12-11')
        mov7.save()
        result.append('Ok')
    except Exception as e:
        return HttpResponse(e)
    context = {
        'ret': result
    }
    return render(request, "ex03/detail.html", context)

def display(request):
    movies =  Movies.objects.all()
    film = []
    for movie in movies:
        film.append((movie.title, movie.episode_nb, movie.opening_crawl, movie.director, movie.producer, movie.release_date ))
    if film == []:
        return HttpResponse("No data available")
    else:
        return render(request, "ex03/display.html", {'film': film})
