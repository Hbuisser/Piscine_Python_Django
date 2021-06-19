#! /bin/sh

python3 -m venv django_env
source django_env/bin/activate
python -m pip install Django
pip freeze > requirement.txt