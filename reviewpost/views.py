from django.shortcuts import render
from django.http import HttpResponse

def signupview(request):
    return render(request, 'reviewpost/signup.html', {'somedate':100})
