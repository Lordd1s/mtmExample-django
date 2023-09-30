from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def news(request: HttpRequest) -> HttpResponse:
    return render(request, 'news.html')