from django.conf import settings
from django.contrib import admin
from django.urls import path, include

api_patterns = (
    [

    ], "api")

# https://docs.djangoproject.com/en/3.2/topics/http/urls/
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include(api_patterns, namespace=settings.API_VERSION_NAMESPACE)),
    path("users/", include(api_patterns, namespace=settings.API_VERSION_NAMESPACE)),
]
