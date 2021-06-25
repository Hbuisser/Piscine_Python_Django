=====
EX00
=====


Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "ex00" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'ex00',
    ]

2. Add the following lines to the settings of your project::

    STATIC_URL = '/ex00/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'ex00/static'),
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'ex00/')

3. Include the polls URLconf in your project urls.py like this::

    path('ex00/', include('ex00.urls')),

4. Run ``python manage.py migrate`` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000 to start the app.