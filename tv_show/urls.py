from django.urls import path, include
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:id>', MovieDetailMovie.as_view(), name='movie_detail'),
    path('movies/add_post/', RewiewCreateView.as_view(), name='create_post'),
    path('movies/<int:id>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/<int:id>/edit/', MovieUpdateView.as_view(), name='edit_movie'),
    path('movie/create/', MovieCreateView.as_view(), name='create_movie'),
    path('movie/search', SearchView.as_view(), name='search')
]