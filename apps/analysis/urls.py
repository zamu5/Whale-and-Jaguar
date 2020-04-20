from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import home

urlpatterns = [
    path('', login_required(home), name='index'),
]