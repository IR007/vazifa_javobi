from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreateForm, CustomUserChangeForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'registration/login.html'
    success_url = 'login'
