from django.urls import path

from . import views

app_name  = 'movie_info'

urlpatterns = [
    path('', views.index),
    path('movie_list/', views.movie_list, name='list'),
    path('movie_list/<int:id>', views.movie_detail, name='detail'),
    path('new_movie/', views.input_movie, name='input')
]