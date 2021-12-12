from django.urls import path

from . import views

app_name  = 'Movie_info'

urlpatterns = [
    path('', views.index),
    path('movie_list/', views.movie_list),
]