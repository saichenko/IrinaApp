from django.contrib import admin
from django.urls import path, include
from irina import urls

urlpatterns = [
    path('', include('irina.urls')),
    path('admin/', admin.site.urls),
]
