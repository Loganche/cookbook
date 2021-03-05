from django.shortcuts import render
from .models import Recipe


def index(request):
    return render(request, 'main/index.html', {'title': 'Main Page'})

def catalogue(request):
    recipes = Recipe.objects.order_by('id')[:10]
    return render(request, 'main/catalogue.html', {'title': 'Catalogue', 'recipes': recipes})

def about(request):
    return render(request, 'main/about.html', {'title': 'About'})