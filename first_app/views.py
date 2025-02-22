from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item


# Create your views here.
def index(response):
    ls = ToDoList(name="take")
    ls.save()

    item = ls.item_set.create(text="django", complete=False)
    item = ls.item_set.create(text="html", complete=False)
    item = ls.item_set.create(text="css", complete=True)
    item = ls.item_set.create(text="javaScript", complete=False)

    return render(response, "first_app/list.html", {"ls": ls})


def about(response, id):
    return HttpResponse(
        "<h1>this is %s page</h1>" % id
    )  # %id is variable from urls.py and %s is placeholder for string variable
