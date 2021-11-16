from django.urls import path
from movies.views import MoviesListView, MovieDetailView, AddReview


urlpatterns = [
    path('', MoviesListView.as_view(), name="movie_list"),
    path('<slug:slug>/', MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
]
