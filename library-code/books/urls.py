from django.urls import path, re_path
from books import views

urlpatterns = [
    path("<str:book_id>", views.HomePageView.as_view(), name='book_info'),
]
