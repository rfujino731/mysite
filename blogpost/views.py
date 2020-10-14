from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import BlogModel

from django.urls import reverse_lazy

class BlogList(ListView):
    template_name = 'blogpost/list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'blogpost/detail.html'
    model = BlogModel

class BlogCreate(CreateView):
    template_name = 'blogpost/create.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')
