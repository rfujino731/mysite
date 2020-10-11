from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogModel

class BlogList(ListView):
    template_name = 'blogpost/list.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name = 'blogpost/detail.html'
    model = BlogModel

# Create your views here.
