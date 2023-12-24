from django.shortcuts import render
from django.views.generic.base import TemplateView, View
import json
import requests
import pages.support_func as sf


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

        start_index = int(request.GET.get('start_index', 0))
        max_results = int(request.GET.get('max_results', 9))

        params = {
            "q": search_query,
            "startIndex": start_index,
            "maxResults": max_results
        }

        if search_query:
            api_response = get_api(params)

            for value in api_response.get('items', []):
                volume_info = value.get("volumeInfo", {})

                result.append(
                    [
                        volume_info.get('title', "Unknown Title"),
                        volume_info.get('subtitle', ""),
                        ''.join(volume_info.get('authors', 'Unknown Author')),
                        value.get('id', "")
                    ]
                )
                # print(volume_info.get('industryIdentifiers')[0]['identifier'])

        context = {
            'result': result,
            "start_index": start_index,
            "max_results": max_results,
            "next_start_index": start_index + max_results,
            "prev_start_index": start_index - max_results,
            "modified_url": sf.remove_parameters(request.get_full_path(), "start_index", "max_results")
        }

        if context.get("prev_start_index") < 0:
            context["prev_start_index"] = 0

        return render(request, template_name="pages/catalog.html", context=context)


def get_api(params=None):
    api = f"https://www.googleapis.com/books/v1/volumes"
    data = requests.get(api, params=params)
    data = data.json()
    return data

