from django.urls import path
from pages import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("catalog/", views.CatalogView.as_view(), name='catalog'),
]
