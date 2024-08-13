
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('<str:author>', views.Author_details,name='author-detail'),
]
