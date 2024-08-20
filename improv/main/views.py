from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "main/index.html", context)

def about(request):
    context = {}
    return render(request, "main/about.html", context)

def shows(request):
    context = {}
    return render(request, "main/shows.html", context)

def players(request):
    context = {}
    return render(request, "main/players.html", context)