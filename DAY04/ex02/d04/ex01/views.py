from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

def django_view(request):
    return render(request, 'django.html')

def display_view(request):
    return render(request, 'display.html')

def templates_view(request):
    return render(request, 'templates.html')