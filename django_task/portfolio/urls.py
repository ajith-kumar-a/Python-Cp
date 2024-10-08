
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page,name='landing-page'),
    path('all-post', views.all_post,name='all-post'),
    path('add-comment', views.AddComment.as_view(),name='add-comment'),
    path('add-post', views.AddPost.as_view(),name='add-post'),
    path('<slug:slugs>', views.user_details_slug,name='user-detail-slug'),
    # path('<int:id>', views.user_details_id,name='user-detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
