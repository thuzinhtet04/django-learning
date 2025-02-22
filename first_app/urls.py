from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # route for /  showing index html
    path(
        "about/<int:id>",
        views.about,
        name="about-us",  # dynamic id form route is passed to view
    ),  # route for /about  showing about html
]
