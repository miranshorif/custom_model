from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    class meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'zep_code']
        error_css_class = 'error'