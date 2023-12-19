from django.urls import path, re_path
from pages import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("catalog/", views.CatalogPageView.as_view(), name='catalog'),
]
