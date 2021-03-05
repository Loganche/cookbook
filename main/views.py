from django.shortcuts import render
from .models import Recipe


def index(request):
    return render(request, 'main/index.html', {'title': 'Main Page'})

def catalogue(request):
    recipes = Recipe.objects.order_by('id')[:10]
    return render(request, 'main/catalogue.html', {'title': 'Catalogue', 'recipes': recipes})

def search(request):
    return render(request, 'main/search.html', {'title': 'Search'})

def profile(request):
    return render(request, 'main/profile.html', {'title': 'Profile'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})