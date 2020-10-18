from django.shortcuts import render
from django.http import HttpResponse

def signupview(request):
    print(request.POST.get('username_date'))
    return render(request, 'reviewpost/signup.html', {'somedate':100})
