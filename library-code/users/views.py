from django.shortcuts import render, redirect
from django.views import View

import pages.support_func as sf


# Check if user is logged in and redirect
def identify(request, *args, **kwargs):
    user = request.user

    if not user.is_anonymous:
        return redirect(f"/users/{user.pk}/")

    return redirect("login")


class UserView(View):

    def get(self, request, *args, **kwargs):

        if request.user.pk != kwargs['user_id']:
            return render(request, 'errors/wrong_user_error.html')

        tbr = dict()

        for book_id in request.user.tbr:
            api_response = sf.get_api(book_id=book_id)
            volume_info = api_response.get('volumeInfo', {})
            book_info = {
                'id': book_id,
                'name': volume_info.get('title')
            }
            tbr[book_id] = book_info

        data = {
            "email": request.user.email,
            "name": request.user.name,
            "user_id": kwargs['user_id'],
            "date_joined": request.user.date_joined,
            "TBR": tbr
        }

        print(request.user.tbr)

        return render(request, template_name="users/user_info.html", context=data)
