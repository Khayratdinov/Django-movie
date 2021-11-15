from django.urls import path
from movies.views import MoviesListView, MovieDetailView


urlpatterns = [
    path('', MoviesListView.as_view(), name="movie_list"),
    path('<slug:slug>/', MovieDetailView.as_view(), name="movie_detail")
]
