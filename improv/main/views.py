from django.shortcuts import render
from .models import Player, Show

from datetime import datetime

def index(request):
    context = {
        "title": "unwritten Improv",
    }
    return render(request, "main/index.html", context)

def about(request):
    context = {
        "title": "About",
    }
    return render(request, "main/about.html", context)

def shows(request):

    context = {
        "title": "Shows",
        "shows": Show.objects.filter(
            time__gte=datetime.now().date()
        ).order_by('time')
    }
    return render(request, "main/shows.html", context)

def players(request):
    context = {
        "title": "Players",
        "players": Player.objects.filter(active=True).order_by('?'),
    }
    print(context["players"][0].photo.url)
    return render(request, "main/players.html", context)