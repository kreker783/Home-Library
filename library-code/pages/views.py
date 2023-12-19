from django.shortcuts import render
from django.views.generic.base import TemplateView, View
import json
import requests


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class BookPageView(View):

    def get(self, request, *args, **kwargs):
        iban = '9781429914567'
        api = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{iban}"
        data = requests.get(api)
        data = data.json()

        data = {
            'data': data['items'][0]['volumeInfo'],
        }

        return render(request, template_name="pages/catalog.html", context=data)


class CatalogPageView(View):

    def get(self, request, *args, **kwargs):
        result = list()

        search_query = request.GET.get('search_query', '')
        search_query = search_query.replace(' ', '+')

        if search_query:
            api_response = get_api(search_query)

            api_response = json.loads(api_response)

            for value in api_response.get('items', []):
                volume_info = value.get("volumeInfo", {})

                result.append(
                    [
                        volume_info.get('title', "Unknown Title"),
                        volume_info.get('subtitle', ""),
                        ''.join(volume_info.get('authors', ''))
                    ]
                )

        return render(request, template_name="pages/catalog.html", context={'result': result})


def get_api(q):
    api = f"https://www.googleapis.com/books/v1/volumes?q={q}"
    data = requests.get(api)
    data = data.json()
    return data
