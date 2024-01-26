from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie, Reviews
from .forms import Form

def movies_list(request):
    movies = Movie.objects.all()
    form = Reviews.objects.all()
    return render(request, 'movies/movies.html',{'movies': movies,
                                                 'form': form})

def movies_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    form = Reviews.objects.all()
    return render(request, 'movies/movies_detail.html', {'movie': movie,
                  'form': form})

def create_post(request):
    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse(f'Успешно добавлено! <a href="/movies">Главная</a>')
    else:
        form = Form()
    return render(request, template_name='movies/crud/comments.html', context={'form': form})


