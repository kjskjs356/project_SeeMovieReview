from django.shortcuts import render
from django.http import JsonResponse
from .models import Movie
import requests

API_KEY = '76c202108d9d00290dcdd6976646a51c'
url = 'https://api.themoviedb.org/3/movie/top_rated?api_key=' + API_KEY + '&language=ko-KR&page=20'
data = requests.get(url).json()

# Create your views here.
def index(request):
    context = {
        'movies': data,
    }
    return render(request, 'movies/index.html', context)


def search(reuest):
    pass