from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usersd.urls', namespace='usersd')),
    path('admin/', admin.site.urls),
]
