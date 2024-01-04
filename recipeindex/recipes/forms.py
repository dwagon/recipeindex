from django import forms
from .models import Authors, Books


class SearchForm(forms.Form):
    text = forms.CharField()


class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ["name"]


class BooksCreateForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["title", "authors"]

    authors = forms.ModelMultipleChoiceField(
        queryset=Authors.objects.all(), widget=forms.CheckboxSelectMultiple
    )


# EOF
