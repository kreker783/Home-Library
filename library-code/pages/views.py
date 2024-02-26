from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic.base import View
import requests
from dotenv import load_dotenv
import os
import pages.support_func as sf


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        load_dotenv()
        api_key = os.getenv('NYTimes_key')

        nytimes_api = f"https://api.nytimes.com/svc/books/v3/lists.json?list-name=hardcover-fiction&api-key="
        nytimes_full_api = nytimes_api + api_key

        response = requests.get(nytimes_full_api)
        print(response.json())
        return render(request, template_name="pages/home.html")


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
            api_response = sf.get_api(params)

            for value in api_response.get('items', []):
                volume_info = value.get("volumeInfo", {})

                authors = volume_info.get('authors')

                in_tbr = False

                if request.user.is_authenticated:
                    if value.get('id', "") in request.user.tbr:
                        in_tbr = True

                result.append(
                    [
                        volume_info.get('title', "Unknown Title"),
                        volume_info.get('subtitle', ""),
                        ', '.join(authors) if authors else 'Unknown Author',
                        value.get('id', ""),
                        volume_info.get('imageLinks', {}).get('thumbnail', None),
                        volume_info.get('averageRating', 0.0),
                        volume_info.get('pageCount'),
                        in_tbr
                    ]
                )

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

    def post(self, request, book_id=None, *args, **kwargs):
        book_id = request.POST.get("book_id")
        if book_id is None:
            return HttpResponseBadRequest("Book ID required")

        if not request.user.is_authenticated:
            error_message = "You must be logged"
            messages.error(request, error_message)
        else:
            if book_id in request.user.tbr:
                request.user.tbr.remove(book_id)
            else:
                request.user.tbr.append(book_id)

            request.user.save()

        return HttpResponseRedirect(request.build_absolute_uri())


