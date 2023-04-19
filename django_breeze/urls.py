from django.urls import path
from django_breeze.views import welcome_page

urlpatterns = [path("", welcome_page, name="welcome")]
