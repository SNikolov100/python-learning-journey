from django.urls import path, include
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>/', include([
        path('', views.show_profile_details, name='details'),
        path('edit/', views.edit_profile, name='edit'),
        path('delete/', views.delete_profile, name='delete')
    ])),
]