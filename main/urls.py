from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='home'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('search', views.search, name='search'),
    path('new', views.new, name='new'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('users', views.users, name='users'),
    path('about', views.about, name='about'),
]