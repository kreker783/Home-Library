from django.urls import path
from users import views

urlpatterns = [
    path("me/", views.UserView.as_view(), name='user_info'),
]
