#from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello, world. You're at the index.")
# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % questoin_id)

def results(request, question_id):
    responce = "You're looking at the results of question %s."
    return HttpResponse(responce % question_id)

def vote(request, question_id):
    return HttpResponse("You're looking at question %s." % questoin_id)