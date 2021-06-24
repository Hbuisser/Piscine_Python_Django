from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .forms import ContactForm
from django.contrib.auth import logout
from django.views.generic import View


class ArticleListView(ListView):
    model = Article
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PublicationView(ListView):
    model = Article
    def get(self, request):
        user = self.request.user
        context = { 'articles': self.model.objects.filter(author=user),
                    'headers':['Title', 'Synopsis', 'Created', 'Detail']}
        return render(request, "article/publication.html", context)

class DetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

