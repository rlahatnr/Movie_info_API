from django.db import models

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

# Create your models here.

# id, title, year, rating, genres, summary
class Movie_data_list(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500)
    year = models.IntegerField()
    rating = models.FloatField()
    genres = models.CharField(max_length=500)
    summary = models.CharField(max_length=3000)


class New_movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    year = models.IntegerField()
    genres = models.CharField(max_length=500)
    summary = models.CharField(max_length=3000)