from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('list/', views.recent_reviews, name='list'),
    path('<int:pk>/', views.review_details, name='details')
]