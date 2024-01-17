from django.urls import path

from home import views

urlpatterns = [
    path('bookskg/', views.books_view, name='books')
]