from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
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


# @require_safe
def detail(request, movie_pk):
    # movie = get_object_or_404(Movie.objects.prefetch_related('genres'), pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


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


def like(request, movie_pk):
    if request.is_ajax():
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {'liked': liked, 'count': movie.like_users.count(),}
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest()