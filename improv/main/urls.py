from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("shows/", views.shows, name="shows"),
    path("about/", views.about, name="about"),
    path("players/", views.players, name="players"),
]