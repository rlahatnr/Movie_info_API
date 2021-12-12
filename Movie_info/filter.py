import django_filters
from django_filters import CharFilter, OrderingFilter
from .models import Movie_data_list

class SortFilter(django_filters.FilterSet):
    CHOICE_FIELD = {
        'descending': '내림차',
        'ascending': '올림차'
    }

    title = CharFilter(field_name='title', lookup_expr='icontains', label='title')
    genres = CharFilter(field_name='genres', lookup_expr='icontains', label='genres')
    rating = OrderingFilter(field_name='rating', fields=(
            ('rating', 'rating'),
        ), label='rating')

    class Meta:
        model = Movie_data_list
        fields = ['year']

