from django.urls import path
from ..rest_api import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list'),
]
