from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'content', 'author']

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')