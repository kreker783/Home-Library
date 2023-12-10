from django.urls import path
from users import views

urlpatterns = [
    path("check_user/", views.identify, name='check_user'),
    path("<int:user_id>/", views.UserView.as_view(), name='user_info'),
]
