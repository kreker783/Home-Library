from django.shortcuts import render
from django.views.generic import View
import pages.support_func as sf

# Create your views here.
class  BookInfoView(View):

    def get(self, request, book_id, *args, **kwargs):
        params = {
            'id': book_id,
        }

        api_response = sf.get_api(params)
        volume_info = api_response.get('volume_info', {})

        result = {
            'title': volume_info.get('title'),
            'authors': ', '.join(volume_info.get('authors')),
            'publisher': volume_info.get('publisher', 'Unknown publisher'),
            'year': volume_info.get('publishedDate'),
            'description': volume_info.get('description', 'Unknown'),
            'pages': volume_info.get('pageCount'),
            'categories': ', '.join(volume_info.get('categories')),
            'rating': volume_info.get('averageRating'),
            'cover': volume_info.get('imageLinks').get('medium'),
            'language': volume_info.get('language', 'Unknown'),
            'price': volume_info.get('retailPrice').get('amount', 'Unknown')
        }


