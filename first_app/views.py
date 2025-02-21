from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("<h1>this is home page</h1>")
def about(response):
    return HttpResponse("<h1>this is about us page</h1>")
