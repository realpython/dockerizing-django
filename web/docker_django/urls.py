from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('docker_django.apps.todo.urls')),
]
