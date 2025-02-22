from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    return HttpResponse("<h1>this is home page</h1>")


def about(response, id):
    return HttpResponse(
        "<h1>this is %s page</h1>" % id
    )  # %id is variable from urls.py and %s is placeholder for string variable
