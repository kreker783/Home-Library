from django.shortcuts import render, redirect
from django.views import View


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

        data = {
            "email": request.user.email,
            "name": request.user.name,
            "user_id": kwargs['user_id'],
            "date_joined": request.user.date_joined
        }
        return render(request, template_name="users/user_info.html", context=data)
