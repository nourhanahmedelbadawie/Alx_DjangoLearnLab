from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(min_value=1900, max_value=2024, required=True)


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
