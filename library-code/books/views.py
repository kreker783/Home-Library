from django.shortcuts import render
from django.views.generic import View
import pages.support_func as sf

import json


class BookInfoView(View):

    def get(self, request, book_id, *args, **kwargs):

        api_response = sf.get_api(book_id=book_id)

        volume_info = api_response.get('volumeInfo', {})
        authors = volume_info.get('authors')

        result = {
            'title': volume_info.get('title'),
            'subtitle': volume_info.get('subtitle', ""),
            'authors': ', '.join(authors) if authors else 'Unknown Author',
            'publisher': volume_info.get('publisher', 'Unknown publisher'),
            'year': volume_info.get('publishedDate'),
            'description': volume_info.get('description', 'Unknown'),
            'pages': volume_info.get('pageCount'),
            'categories': ', '.join(volume_info.get('categories', "")),
            'rating': volume_info.get('averageRating', 0.0),
            'cover': volume_info.get('imageLinks', {}).get('thumbnail', None),
            'language': volume_info.get('language', 'Unknown'),
            'price': api_response.get('retailPrice', {}).get('amount', 'Unknown')
        }

        return render(request, 'books/book_info.html', context=result)
