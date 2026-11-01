from django.urls import path, include
from books import views

app_name = 'books'

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('books/', include([
        path('', views.book_list, name="list"),
        path('<slug:slug>/', views.book_detail, name='detail')
    ]))

]