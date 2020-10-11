from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('list/', BlogList.as_view()),
    path('detail/<int:pk>', BlogDetail.as_view()),
]