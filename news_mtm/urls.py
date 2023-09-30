from django.urls import path
from news_mtm import views

urlpatterns = [
    path("", views.news, name="news"),
]