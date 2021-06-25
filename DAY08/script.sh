# python3 -m venv ./my_venv
# source ./my_venv/bin/activate
# python3 -m pip install -r requirement.txt
brew install nginx
brew services start nginx
cp ./d08/d08_nginx.conf ~/.brew/etc/nginx/servers/
brew services restart nginx
python3 -m pip install gunicorn
gunicorn -c ./d08/gunicorn_config.py d08.wsgi
nginx
# brew install nginx uwsgi uwsgi-plugin-python3
# mkdir -p /home/ubuntu/static /home/ubuntu/media
# chown www-data.www-data /home/ubuntu/media
# ./manage.py collectstatic