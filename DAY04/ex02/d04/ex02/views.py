from django.shortcuts import render
from .forms import MyForm
from datetime import datetime
import logging
import sys

# Create your views here.
def base(request):
    return render(request, 'base.html')

def create_view(request):
    my_form = MyForm()
    if request.method == "POST":
        my_form = MyForm(request.POST)
        if my_form.is_valid():
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            x = my_form.cleaned_data['title']
            with open("ex02/input.logs", 'a+') as f:
                f.write(x + " - " + dt_string)
                
        else:
            print(my_form.errors)
    else:
        my_form = MyForm
    ret = ""
    try:
        file = open("ex02/input.logs", "r")
        ret = file.readlines()
        file.close()
    except:
        print("Wrong file ")
    context = {
        "form": my_form,
        "ret": ret
    }
    return render(request, "form.html", context)




# # Create your views here.
# logger = logging.getLogger(__name__)
# def ex02(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             logger.debug(form.cleaned_data['subject'])
