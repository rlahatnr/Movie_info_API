from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from .forms import *
from .filter import SortFilter
from django.views.generic.edit import CreateView

def movie_list(request):
    data = Movie_data_list.objects.all()

    filter = SortFilter(request.GET, queryset=data)
    data = filter.qs

    page = request.GET.get('page', '1')
    paginator = Paginator(data, 10)
    page_obj = paginator.get_page(page)

    context = {'data': page_obj, 'page': page, 'filter':filter}
    return render(request, 'Movie_info/movie_list.html', context)

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

def movie_detail(request, id):
    data = Movie_data_list.objects.filter(id=id)
    review = Movie_review.objects.filter(movie_id=id)

    for i in review:
        if request.method == 'POST' and f'delete {i.review_id}' in request.POST:
            data = Movie_review.objects.get(review_id=i.review_id)
            print(i.review_id)
            data.delete()
            return HttpResponseRedirect(request.path_info)

    if request.method == 'POST':
        form = Review_form(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.movie_id = Movie_data_list.objects.get(id=id)
            f.save()
            return HttpResponseRedirect('%i' % id)
    else:
        form = Review_form()

    context = {'data': data, 'review': review, 'form':form}
    return render(request, 'Movie_info/movie_detail.html', context)

