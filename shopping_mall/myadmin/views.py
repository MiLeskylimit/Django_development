from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def t(request):
    return HttpResponse("Hello myadmin!")
