from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View


# Create your views here.
class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html')

    def post(self, request, *args, **kwargs):
        data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }

        user = authenticate(request, username=data.get('email'), password=data.get('password'))

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("home")
        else:
            messages.error(request, 'Invalid login credentials.')

        return redirect("login")

