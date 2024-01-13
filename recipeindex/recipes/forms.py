from django import forms
from django.urls import reverse_lazy
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, MultiWidgetField
from crispy_forms.bootstrap import InlineRadios
from crispy_bootstrap5.bootstrap5 import FloatingField
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


class XRecipesCreateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "ingredients", "book"]

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredients.objects.all(), widget=forms.CheckboxSelectMultiple
    )


class RecipesCreateForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = "__all__"
        widgets = {
            "book": forms.RadioSelect,
            "ingredients": autocomplete.ModelSelect2Multiple(
                url="recipes:ingredient-autocomplete"
            ),
        }


# EOF
