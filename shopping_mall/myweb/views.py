from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def t(requst):
    return HttpResponse("Hello myweb!")

def t2(request):
    return render(request, "./myweb/test.html")