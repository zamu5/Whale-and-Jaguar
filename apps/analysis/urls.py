from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import home, aboutus

urlpatterns = [
    path('', login_required(home), name='home'),
    path('aboutus', login_required(aboutus), name='aboutus'),

]