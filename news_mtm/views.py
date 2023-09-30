from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from news_mtm import models


# Create your views here.
def news(request: HttpRequest) -> HttpResponse:
    news = models.News.objects.all()
    return render(request, 'news.html', {'news': news})

