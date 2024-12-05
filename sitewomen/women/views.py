from django.http import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse("Страница приложения women")

def categories(request):
    return HttpResponse("<h1>Статьи по катеригориям</h1>")

def main(request):
    return HttpResponse("<h1>Главная Страница</h1>")
"""раскумар"""
"""раскумар"""
"""раскумар3"""