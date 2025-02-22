from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.
def index(response):
    t = ToDoList.objects.get(name="Take")

    item = t.item_set.create(text="django", complete=False)

    return HttpResponse("<h1>this is %s page</h1>" % item)


def about(response, id):
    return HttpResponse(
        "<h1>this is %s page</h1>" % id
    )  # %id is variable from urls.py and %s is placeholder for string variable
