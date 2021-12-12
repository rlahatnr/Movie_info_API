from django.db import models

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# Create your models here.

# id, title, year, rating, genres, summary
class Movie_data_list(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField(default=0.0)
    genres = models.CharField(max_length=255)
    summary = models.CharField(max_length=1500)


class Movie_review(models.Model):
    movie_id = models.ForeignKey(Movie_data_list, on_delete=models.CASCADE)
    review_id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=1500)
    rating = models.IntegerField()
