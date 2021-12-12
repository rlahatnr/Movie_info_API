from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Movie_data_list
from django.core.paginator import Paginator
from .forms import Input_new_form
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

def movie_detail(request, id):
    data = Movie_data_list.objects.filter(id=id)
    context={'data':data}
    return render(request, 'Movie_info/movie_detail.html', context)

def input_movie(request):
    if request.method == 'POST':
        form = Input_new_form(request.POST)
        if form.is_valid():
            data = form.save()
            return HttpResponseRedirect('movie_list/%i' % data.id)
    else:
        form = Input_new_form()
    context = {'form': form}
    return render(request, 'Movie_info/new_movie.html', context)
