from django.urls import path, include
from .views import dashboard, destinations_list, destination_details

app_name = 'destinations'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('destinations/', include([
        path('', destinations_list, name='list'),
        path('<slug:slug>/', destination_details, name='detail')
    ]))
]