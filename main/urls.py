from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('search', views.search, name='search'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
]