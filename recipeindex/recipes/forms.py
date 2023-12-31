from django import forms
from .models import Authors


class SearchForm(forms.Form):
    text = forms.CharField()


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ["name"]
