from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from movies.models import Movie
# Create your views here.

class MoviesListView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)

class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    slug_field = "slug"

