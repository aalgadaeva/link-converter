from django.forms import ModelForm
from django import forms
from .models import Converter

class ConvertForm(forms.ModelForm):
    link = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        widget=forms.TextInput(
        attrs={'placeholder': '*Paste link here...',
               'class': 'form-control mt-3',
               }
    ), label='')

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': '*Email',
               'class': 'form-control mt-4',
               }
    ), label='')

    class Meta:
        model = Converter
        fields = ['link', 'email',]