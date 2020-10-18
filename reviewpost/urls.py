from django.urls import path
from .views import signupview

urlpatterns = [
    path('signup/', signupview, name='signup'),
]