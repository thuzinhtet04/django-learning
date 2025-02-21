from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "index"), #route for /  showing index html 
    path("about/" , views.about , name = "about-us"),  #route for /about  showing about html 
]

