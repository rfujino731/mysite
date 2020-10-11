from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate

urlpatterns = [
    path('list/', BlogList.as_view()),
    path('detail/<int:pk>', BlogDetail.as_view()),
    path('create/', BlogCreate.as_view()),
]