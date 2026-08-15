from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content', 'author']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'content']