from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def search(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/search.html', context)


def like(request):
    pass