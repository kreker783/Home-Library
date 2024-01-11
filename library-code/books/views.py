from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

import pages.support_func as sf


class BookInfoView(View):

    def get(self, request, book_id, *args, **kwargs):

        api_response = sf.get_api(book_id=book_id)
        volume_info = api_response.get('volumeInfo', {})

        result = {
            'title': volume_info.get('title'),
            'subtitle': volume_info.get('subtitle', ""),
            'authors': volume_info.get('authors', "Unknown author"),
            'publisher': volume_info.get('publisher', 'Unknown publisher'),
            'year': volume_info.get('publishedDate'),
            'description': volume_info.get('description', 'Unknown'),
            'pages': volume_info.get('pageCount'),
            'categories': volume_info.get('categories', ""),
            'rating': volume_info.get('averageRating', 0.0),
            'cover': volume_info.get('imageLinks', {}).get('thumbnail', None),
            'language': volume_info.get('language', 'Unknown'),
        }

        return render(request, 'books/book_info.html', context=result)

    def post(self, request, book_id, *args, **kwargs):
        if not request.user.is_authenticated:
            error_message = "You must be logged"
            messages.error(request, error_message)
        else:
            request.user.tbr.append(book_id)
            request.user.save()
            messages.success(request, "Book has been added to your TBR list")

        return redirect('book_info', book_id=book_id)
