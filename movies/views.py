from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie
from django.http import JsonResponse
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        movies = Movie.objects.all()
        context = {
            'movies': movies,
        }
        return render(request, 'movies/index.html', context)
    return redirect('accounts:login')


def detail(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        context = {
            'movie': movie,
        }
        return render(request, 'movies/detail.html', context)
    return redirect('accounts:login')


def search(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            searched = request.POST['search']
            User = get_user_model()
            users = User.objects.filter(username__contains=searched)
            movies = Movie.objects.filter(title__contains=searched)
            return render(request, 'movies/search.html', {'searched': searched, 'movies': movies, 'users': users,})
        return render(request, 'movies/search.html')
    return redirect('accounts:login')


def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)

        if movie.like_users.filter(pk=request.user.pk).exists():
            # 좋아요 취소
            movie.like_users.remove(request.user)
            liked = False
        else:
            # 좋아요 누름
            movie.like_users.add(request.user)
            liked = True

        data = {
            'liked':liked,
            'like_count':movie.like_users.count(),
        }
        return JsonResponse(data)
    return redirect('accounts:login')


def likelist(request, username):
    if request.user.is_authenticated:
        User = get_user_model()
        person = User.objects.get(username=username)
        context = {
            'person': person,
        }
        return render(request, 'movies/likelist.html', context)
    return redirect('accounts:login')