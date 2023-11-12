from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'event'

urlpatterns = [
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='event_create'),
    path('', views.event_list, name='event_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
