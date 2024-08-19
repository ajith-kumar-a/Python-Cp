from django.urls import path
from . import views
urlpatterns = [
    path('',views.feedbackform),
    path('thankyou',views.thanku)
 
]
 