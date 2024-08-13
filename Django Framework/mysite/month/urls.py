
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index),
    path('aji',views.ajith),
    path('<int:month>', views.monthly_details_num),
    path('<str:month>', views.monthly_details,name='month-detail'),
]
