from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('searched/', views.searched, name='searched'),
    path('like/<str:username>/', views.like, name='like'),
]
