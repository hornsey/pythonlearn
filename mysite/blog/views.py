from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<html>Hello World!</html>')

def hello1(request):
    return HttpResponse('<html>Hello World!New request.</html>')