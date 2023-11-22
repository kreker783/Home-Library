from django.urls import path
from auth import views

urlpatterns = [
    path("login/", views.LoginPageView.as_view(), name='login')
]