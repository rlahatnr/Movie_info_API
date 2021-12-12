from django.http import HttpResponse
from .models import Movie_data_list
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from .filter import SortFilter


def index(request):
    return HttpResponse("안녕하세요 movie_info에 오신것을 환영합니다.")

def movie_list(request):
    data = Movie_data_list.objects.all()

    filter = SortFilter(request.GET, queryset=data)
    data = filter.qs

    page = request.GET.get('page', '1')
    paginator = Paginator(data, 10)
    page_obj = paginator.get_page(page)

    context = {'data': page_obj, 'page': page, 'filter':filter}
    return render(request, 'Movie_info/movie_list.html', context)
