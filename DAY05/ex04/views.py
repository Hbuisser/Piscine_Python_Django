from django.shortcuts import render
from psycopg2 import connect, extensions, sql
import psycopg2
import sys
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden)

# Create your views here.

class DataBase():
    def access_db(self):
        try:
            conn = connect(
                dbname = "djangotraining",
                user = "djangouser",
                host = "localhost",
                password = "secret"
                )
        except psycopg2.DatabaseError as e:
            return HttpResponse(e)
        return conn
        
    def create_tab(self, conn, name):
        mycursor = conn.cursor()
        mycursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                title varchar(64) NOT NULL,
                episode_nb int PRIMARY KEY, 
                opening_crawl text,
                director varchar(32) NOT NULL,
                producer varchar(128) NOT NULL,
                release_date date NOT NULL
                )""".format(name))
        conn.commit()
        conn.close()

    def excec_query(self, conn, name, query):
        mycursor = conn.cursor()
        mycursor.execute(query)
        i = mycursor.rowcount
        conn.commit()
        return i

def create_table(request):
    obj = DataBase()
    try:
        conn = obj.access_db()
        obj.create_tab(conn, "ex04_movies")
    except psycopg2.DatabaseError as e:
        return HttpResponse(e)
    return render(request, 'ex04/index04.html')

def populate(request):
    name = "ex04_movies"
    obj = DataBase()
    ret_str = ""
    try:
        conn = obj.access_db()
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('1', 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('2', 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('3', 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('4', 'A New Hope', 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('5', 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('6', 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
        query = """ INSERT INTO ex04_movies (episode_nb, title, director, producer, release_date)
                    VALUES ('7', 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
                    ON CONFLICT (episode_nb) DO NOTHING
                """
        i = obj.excec_query(conn, name, query)
        if i > 0:
            ret_str += "Ok \n"
    except psycopg2.DatabaseError as e:
        return HttpResponse(e)
    context = {
        'ret': ret_str
    }
    return render(request, "ex04/detail.html", context)

def display(request):
    name = "ex04_movies"
    obj = DataBase()
    context = {}
    try:
        conn = obj.access_db()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM {}".format(name))
        myresult = mycursor.fetchall()
        context['film'] = myresult
    except psycopg2.DatabaseError as e:
        return HttpResponse(e)
    if myresult == []:
        return HttpResponse("No data available")
    else:
        return render(request, "ex04/display.html", context)

def remove(request):
    obj = DataBase()
    name = "ex04_movies"
    if request.method == 'POST':
        title = request.POST['Key']
        title = f"'{title}'"
        try:
            conn = obj.access_db()
            mycursor = conn.cursor()
            mycursor.execute("DELETE FROM {} WHERE title = {}".format(name, title))
            conn.commit()
        except psycopg2.DatabaseError as e:
            return HttpResponse(e)
    context = []
    try:
        conn = obj.access_db()
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM {}".format(name))
        myresult = mycursor.fetchall()
        for result in myresult:
            context.append(result[0])
    except psycopg2.DatabaseError as e:
        return e
    if myresult == []:
        return HttpResponse("No data available")
    else:
        return render(request, "ex04/remove.html", {'film': context})