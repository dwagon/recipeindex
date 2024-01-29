from django import forms
from dal import autocomplete
from .models import Authors, Books, Ingredients, Recipes


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


class RecipesCreateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "book", "ingredients"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "p-2 mb-4 form-control"}),
            "book": forms.RadioSelect(attrs={"class": "p-2"}),
            "ingredients": autocomplete.ModelSelect2Multiple(
                url="recipes:ingredient-autocomplete",
                attrs={"class": "p-2 form-control"},
            ),
        }


class RecipesCreateBookForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "book", "ingredients"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "p-2 mb-4 form-control"}),
            "book": forms.HiddenInput,
            "ingredients": autocomplete.ModelSelect2Multiple(
                url="recipes:ingredient-autocomplete",
                attrs={"class": "p-2 form-control"},
            ),
        }


# EOF
