from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('like/<int:photo_id>/', views.like_functionality_view, name='like'),
    path('share/<int:photo_id>/', views.share_functionality, name='share')
]
