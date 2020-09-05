from django.http import HttpResponse
from django.shortcuts import render


def first_attempt(request):
    return HttpResponse(content=render(request, 'index.html'))