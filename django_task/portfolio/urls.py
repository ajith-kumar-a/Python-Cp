
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('<int:id>', views.user_details_id,name='user-detail'),

    path('all-post', views.all_post,name='all-post'),

]
