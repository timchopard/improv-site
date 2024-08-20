from django.shortcuts import render
from .models import Player, Show

from datetime import datetime

def index(request):
    context = {}
    return render(request, "main/index.html", context)

def about(request):
    context = {}
    return render(request, "main/about.html", context)

def shows(request):

    context = {
        "shows": Show.objects.filter(
            time__gte=datetime.now().date()
        ).order_by('time')
    }
    return render(request, "main/shows.html", context)

def players(request):
    context = {
        "players": Player.objects.filter(active=True).order_by('?'),
    }
    print(context["players"][0].photo.url)
    return render(request, "main/players.html", context)