from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),

    path('event/', include('event.urls', namespace='event')),
    path('team/', include('team.urls', namespace='team')),

    path('about/', include('about.urls', namespace='about')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
]
