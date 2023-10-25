from django.urls import path
from . import views

app_name = 'event'

urlpatterns = [
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='event_create'),
    path('', views.event_list, name='event_list'),
]
