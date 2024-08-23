from django.urls import path
from .import views
 
urlpatterns = [
    path('',views.CreateProfileView.as_view()),
    path('renderingImg',views.Profileview.as_view())
]