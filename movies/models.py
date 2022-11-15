from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    poster_url = models.TextField()