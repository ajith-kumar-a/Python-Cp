from django.urls import path  
from .views import image_request  
  
app_name = 'PortfolioDetails'  
urlpatterns = [  
    path('', image_request, name = "image-request")  
]