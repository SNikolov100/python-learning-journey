from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.books_home, name='home'),
    path('list/', views.books_list, name='list'),
    path('create/', views.book_create, name='create'),
    path('<int:pk>/details/', views.books_details, name='details')
]