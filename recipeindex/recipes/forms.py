from django import forms
from django.urls import reverse_lazy
from .models import Authors, Books, Ingredients, Recipes
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_forms.bootstrap import InlineRadios, InlineCheckboxes
from crispy_bootstrap5.bootstrap5 import FloatingField


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
            "ingredients": forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse_lazy("recipes:recipes_create")
        self.helper.layout = Layout(
            Row(Column(FloatingField("name"))),
            Row(Column(InlineRadios("book"))),
            Row(
                Submit(
                    "submit",
                    "Create Recipe",
                    field_classes="btn",
                    css_class="p-2",
                ),
                css_class="form_row",
            ),
            Row(Column(InlineCheckboxes("ingredients", css_class="p-2"))),
        )


# EOF
