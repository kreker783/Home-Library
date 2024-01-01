from django.urls import path, include
from pages import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("catalog/", views.CatalogPageView.as_view(), name='catalog'),
    path("catalog/book/", include('books.urls'))
]
