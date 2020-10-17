from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

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

class BlogDelete(DeleteView):
    template_name = 'blogpost/delete.html'
    model = BlogModel
    success_url = reverse_lazy('list')

class BlogUpdate(UpdateView):
    template_name = 'blogpost/update.html'
    model = BlogModel
    fields = ('title', 'content', 'category')
    success_url = reverse_lazy('list')