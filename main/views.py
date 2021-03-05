from django.shortcuts import render, redirect

from .forms import RecipeForm, SignUpForm
from .models import Recipe


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'main/index.html', context)


def catalogue(request):
    recipes = Recipe.objects.order_by('id')[:10]
    context = {
        'title': 'Catalogue',
        'recipes': recipes
    }
    return render(request, 'main/catalogue.html', context)


def search(request):
    context = {
        'title': 'Search',
    }
    return render(request, 'main/search.html', context)


def new(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:catalogue')
        else:
            error = 'Wrong input.'

    form = RecipeForm
    context = {
        'title': 'Edit recipe',
        'form': form,
        'error': error
    }
    return render(request, 'main/new.html', context)


def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'main/profile.html', context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'main/about.html', context)


def signup(request):
    error = ''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
        else:
            error = 'Wrong input.'

    form = SignUpForm
    context = {
        'title': 'Sign up',
        'form': form,
        'error': error
    }
    return render(request, 'main/signup.html', context)
