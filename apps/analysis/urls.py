from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import index
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', login_required(index), name='home'),
]