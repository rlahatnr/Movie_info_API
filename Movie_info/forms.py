from django import forms
from .models import New_movie


class Input_new_form(forms.ModelForm):
    class Meta:
        model = New_movie
        fields = ['title', 'year', 'genres', 'summary']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'genres': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.URLInput(attrs={'class': 'form-control'}),
        }

        required = "__all__"