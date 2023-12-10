from django.urls import path
from auth import views

urlpatterns = [
    path("login/", views.LoginPageView.as_view(), name='login'),
    path("register/", views.RegisterPageView.as_view(), name='register'),
    path("logout/", views.LogoutView.as_view(), name='log_out'),
]
