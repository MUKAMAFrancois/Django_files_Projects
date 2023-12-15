from django.shortcuts import render,redirect
from .models import Article
from django.views.generic import ListView,DetailView,DeleteView,TemplateView
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.urls import reverse_lazy


class Index(ListView):
    model=Article
    queryset=Article.objects.all().order_by('-date')
    template_name='postapp/index.html'
    paginate_by=3

class InDetails(DetailView):
    model=Article
    template_name='postapp/detail_article.html'

class ScienceRelated(ListView):
        model=Article
        queryset=Article.objects.filter(sciences=True).order_by('-date')
        template_name='postapp/sciences.html'
        paginate_by=1
class CompleteDelete(TemplateView):
     template_name='postapp/deleted.html'
class DeleteArticle(DeleteView):
     model=Article
     template_name='postapp/delete_article.html'
     success_url=reverse_lazy('compeletely_deleted')

class AddArticle(CreateView):
     model=Article
     template_name='postapp/addnew.html'
     fields=['title','author','sciences','content']
     success_url=reverse_lazy('index')

class EditArticle(UpdateView):
     model=Article
     template_name='postapp/edit_article.html'
     fields=['title','sciences','content']
     success_url=reverse_lazy('index')
