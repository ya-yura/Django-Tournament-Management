from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('create/', views.create_team, name='create_team'),
    path('<int:pk>/', views.team_detail, name='team_detail'),
    path('', views.team_list, name='team_list'),
    path('join/<uuid:invite_link>/', views.join_team, name='join_team'),
]
