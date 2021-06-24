from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, UserFavoriteArticle
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
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
    
    def post(self, request):
        tmp = UserFavoriteArticle.objects.filter(user=request.user)
        exist = False
        id_ = request.POST('id')
        print(id_)
        for art in tmp:
            if art.article.id == id_:
                exist = True
                break
        if not exist:
            art = Article.objects.filter(id=id_)
            usr = request.user
            form = UserFavoriteArticle(user=usr, article=art[0])
            form.save()
            messages.success(self.request, f'The Article Is Now In Your Favorite!')
        else:
            messages.error(self.request, f'The Article Is Already in Your Favorite!')
        return redirect('')

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

class FavoritesView(ListView):
    template_name = 'article/article_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.request.user)
    #     if self.request.user.is_authenticated:
    #         context['latest_articles'] = UserFavoriteArticle.objects.filter(user=self.request.user)
    #         return context
    #     else:
    #         context['latest_articles'] = 0
    #         return context
    def get_queryset(self):
        queryset = UserFavoriteArticle.objects.filter(user = self.request.user)
        return queryset

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)