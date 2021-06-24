from django.shortcuts import render
from .forms import MyForm
from datetime import datetime
import logging
import pytz
import sys
from django.conf import settings

# Create your views here.
# def base(request):
#     return render(request, 'base.html')

def create_view(request):
    my_form = MyForm()
    if request.method == "POST":
        my_form = MyForm(request.POST)
        if my_form.is_valid():
            tz = pytz.timezone('Europe/Brussels')
            dt_string = str(datetime.now(tz))[:19]
            x = my_form.cleaned_data['title']
            with open(settings.LOG_FILE_PATH, 'a+') as f:
                f.write(dt_string + " - " + x + "  " + '\n')
                f.close()
        else:
            print(my_form.errors)
    else:
        my_form = MyForm
    ret = ""
    try:
        file = open(settings.LOG_FILE_PATH, "r")
        ret = file.readlines()
        file.close()
    except:
        print("Wrong file ")
    context = {
        "form": my_form,
        "ret": ret
    }
    return render(request, "form.html", context)

