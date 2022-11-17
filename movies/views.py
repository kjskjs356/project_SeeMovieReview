from django.shortcuts import redirect, render
from django.core import serializers
from django.http import JsonResponse
from .models import Movie


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all()
        context = {
            'movies': movies,
        }
        return render(request, 'movies/index.html', context)
    else:
        return redirect('accounts:login')


def search(request):
    if request.user.is_authenticated:
        return render(request, 'movies/search.html')
    else:
        return redirect('accounts:login')


def searched(request):
    if request.method == 'POST':
        searched = request.POST['search']
        movies = Movie.objects.filter(title__contains=searched)
        return render(request, 'movies/searched.html', {'searched': searched, 'movies': movies})
    else:
        return render(request, 'movies/searched.html', {})


def like(request):
    if request.user.is_authenticated:
        return render(request, 'movies/like.html')
    else:
        return redirect('accounts:login')