from django.urls import path
from . import views
urlpatterns = [
    path('',views.FormsViews.as_view()),
    path('thankyou',views.feedbacklistView.as_view())
 
]
 