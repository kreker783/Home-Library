from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views import View

from .validation import if_data_valid


class RegisterPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/register.html')

    def post(self, request, *args, **kwargs):
        data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'password-confirm': request.POST.get('password-conf')
        }

        if not if_data_valid(data)[0]:
            return render(request, "auth/register.html", if_data_valid(data)[1])

        User = get_user_model()
        user = User.objects.create_user(email=data.get('email'), password=data.get('password'))

        if user is not None:
            login(request, user)
            return redirect("home")

        return redirect("register")


class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html', context=dict(args))

    def post(self, request, *args, **kwargs):
        data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }

        user = authenticate(request, username=data.get('email'), password=data.get('password'))

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, 'auth/login.html', context={'message': 'Wrong credentials!'})


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")
