from django.urls import path
import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("login/", views.LoginPageView.as_view(), name='login')
]
