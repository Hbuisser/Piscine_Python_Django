from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
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

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class PublicationView(ListView):
    model = Article
    def get(self, request):
        user = self.request.user
        print(self.model.objects.filter(author=user))
        context = { 'articles': self.model.objects.filter(author=user),
                    'headers':['Title', 'Synopsis', 'Created', 'Detail']}
        return render(request, "article/publication.html", context)

class DetailView(ListView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'article/article_detail.html'
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id)
    # def get(self, request):
    #     context = {
    #     }
    #     return render(request, "article/detail.html", context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)



# Create your views here.
# def dynamic_lookup_view(request, my_id):
#     # art = Article.objects.get(id=my_id)
#     art = get_object_or_404(Article, id=my_id)
#     context = {
#         'article': art
#     }
#     return render (request, "article/article_detail.html", context)


# class ArticleListView(ListView):
#     queryset = Article.objects.all()