from django.shortcuts import render
from psycopg2 import connect, extensions, sql
import sys

# brew install postgresql
# brew services start postgresql
# psql postgres

# https://kb.objectrocket.com/postgresql/create-a-postgresql-database-using-the-psycopg2-python-library-755

def create_table(request):
    try:
        conn = connect(
            dbname = "djangotraining",
            user = "djangouser",
            host = "localhost",
            password = "secret"
            )
    except psycopg2.DatabaseError as e:
        print(f'Error {e}')
        sys.exit(1)
    mycursor = conn.cursor()
    mycursor.execute("""CREATE TABLE IF NOT EXISTS ex00_movies (
			title varchar(64) NOT NULL,
			episode_nb int PRIMARY KEY, 
			opening_crawl text,
			director varchar(32) NOT NULL,
			producer varchar(128) NOT NULL,
			release_date date NOT NULL
			)""")
    conn.commit()
    conn.close()
    return render(request, 'ex00/index.html')

