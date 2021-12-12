from django import forms
from .models import Movie_data_list, Movie_review


class Input_new_form(forms.ModelForm):
    class Meta:
        model = Movie_data_list
        fields = ['title', 'year', 'genres', 'summary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
        }

        required = "__all__"


class Review_form(forms.ModelForm):
    class Meta:
        model = Movie_review
        fields = ['rating', 'text']
        widgets = {
            'rating': forms.Select(choices= ((str(x), x) for x in range(1,11)), attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'rating':'평점',
            'text': '댓글내용',

        }
        required = "__all__"
