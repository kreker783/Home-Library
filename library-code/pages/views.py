from django.shortcuts import render
from django.views.generic.base import TemplateView, View
import json
import requests


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class CatalogView(View):

    def get(self, request, *args, **kwargs):
        api = "https://www.googleapis.com/books/v1/volumes?q=isbn:9781429914567"
        data = requests.get(api)
        data = data.json()

        # data = json.loads(data['items'][0])
        data = {
            'data': data['items'][0]['volumeInfo'],
        }

        return render(request, template_name="pages/catalog.html", context=data)
