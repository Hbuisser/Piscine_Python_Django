from django.shortcuts import render
from .forms import ArticleForm
from .models import Article
from PIL import Image
import os
from django.views.generic import DetailView, FormView,ListView
# Create your views here.

def index(request):
	context = {}
	obj = {}
	if request.method == "POST":
		form = ArticleForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data.get("title")
			img = form.cleaned_data.get("pics")
			obj=Article.objects.create(
				title = name,
				pics = img
			)
			obj.save()
	else:
		form = ArticleForm()
	obj = Article.objects.all()
		
	context = {
		'article_form' : form,
		'data' : obj
	}
	return render(request, 'index.html', context)