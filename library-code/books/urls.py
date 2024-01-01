from django.urls import path
from books import views

urlpatterns = [
    path("<str:book_id>", views.BookInfoView.as_view(), name='book_info'),
]
