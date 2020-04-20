from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import RegisterForm


class UserRegister(CreateView):
    model = User
    template_name = 'sing_up.html'
    form_class = RegisterForm
    success_url = reverse_lazy('task_list')
