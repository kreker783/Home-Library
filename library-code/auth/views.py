from django.shortcuts import render
from django.views import View


# Create your views here.
class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html')


    def post(self, request, *args, **kwargs):
        
