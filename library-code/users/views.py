from django.shortcuts import render
from django.views import View


# Create your views here.
class UserView(View):

    def get(self, request, *args, **kwargs):
        user = {
            "user": request.user.email
        }
        return render(request, template_name="users/user_info.html", context=user)