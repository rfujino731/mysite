from django.shortcuts import render
from django.http import HttpResponse

def signupview(request):
    return render(request, 'signup.html', {'somedate':100})
