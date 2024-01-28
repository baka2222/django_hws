from django.urls import path, include
from .views import movies_list, movies_detail, create_post

urlpatterns = [
    path('', movies_list),
    path('movies/<int:id>', movies_detail),
    path('movies/add_post/', create_post, name='create_post')
]