from django.urls import path
from user.rest_api import views

urlpatterns = [
    path('', views.UserListCreateAPIView.as_view(), name='users'),

]
