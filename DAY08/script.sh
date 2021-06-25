
python -m pip install django-ex00/dist/django-ex00-0.1.tar.gz
python manage.py collectstatic

brew install nginx
brew services start nginx
cp ./configs/d08_nginx.conf ~/.brew/etc/nginx/servers/
brew services restart nginx

python3 -m pip install gunicorn
gunicorn -c ./configs/gunicorn_config.py d08.wsgi

nginx

