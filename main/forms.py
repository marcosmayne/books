from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.fields import EmailField
from django.forms.forms import Form

from main.models import Author, Book, Genre, Publisher


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        #fields = '__all__'
        fields = ['title', 'sub_title', 'author', 'publisher', 'genre', 'status', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the title of the book'}),
            'sub_title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the subtitle of the book'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'publisher': forms.Select(attrs={'class':'form-control'}),
            'genre': forms.Select(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'})
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'
