from django.shortcuts import render
from django.views.generic.base import TemplateView, View


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'pages/login.html')
