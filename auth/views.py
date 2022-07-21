from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView as Logout

# Remember: Auth doesn't use the db. So no need to include it
# in installed apps of settings.py
# Create your views here.


class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
