from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]
        labels = {
            'first_name': 'Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'username': 'Username',
        }
