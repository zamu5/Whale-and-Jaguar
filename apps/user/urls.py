from django.urls import path, include
from .views import UserRegister

urlpatterns = [
    path('create', UserRegister.as_view(), name='create_user'),
]