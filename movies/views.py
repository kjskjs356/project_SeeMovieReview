from django.shortcuts import render, get_object_or_404
# from django.views.decorators.http import require_safe
from django.http import JsonResponse
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


# @require_safe
def detail(request, movie_pk):
    # movie = get_object_or_404(Movie.objects.prefetch_related('genres'), pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


def search(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/search.html', context)


def like(request):
    pass