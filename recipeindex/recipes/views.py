from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from view_breadcrumbs import (
    DetailBreadcrumbMixin,
    ListBreadcrumbMixin,
    BaseBreadcrumbMixin,
)
from .forms import SearchForm, AuthorCreateForm
from .models import Ingredients, Recipes, Books, Authors


class IndexView(BaseBreadcrumbMixin, TemplateView):
    template_name = "index.html"
    crumbs = []


def search(request):
    """Find a recipe with ingredients"""
    context = {}
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            context["search_term"] = form.cleaned_data["text"]
            context["authors"] = Authors.objects.filter(
                name__contains=form.cleaned_data["text"]
            )
            context["books"] = Books.objects.filter(
                title__contains=form.cleaned_data["text"]
            )
            context["recipes"] = Recipes.objects.filter(
                name__contains=form.cleaned_data["text"]
            )
            context["ingredients"] = Ingredients.objects.filter(
                name__contains=form.cleaned_data["text"]
            )
    else:
        form = SearchForm()

    context["form"] = form
    return render(request, "search.html", context)


class IngredientsListView(ListBreadcrumbMixin, ListView):
    model = Ingredients


class IngredientsDetailView(DetailView, DetailBreadcrumbMixin):
    model = Ingredients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(ingredients=self.object)
        return context


class RecipesListView(ListBreadcrumbMixin, ListView):
    model = Recipes


class RecipesDetailView(DetailBreadcrumbMixin, DetailView):
    model = Recipes


class BooksListView(ListBreadcrumbMixin, ListView):
    model = Books


class BooksDetailView(DetailBreadcrumbMixin, DetailView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(book=self.object)
        return context


class AuthorsListView(ListBreadcrumbMixin, ListView):
    model = Authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AuthorCreateForm()
        return context


class AuthorsDetailView(DetailBreadcrumbMixin, DetailView):
    model = Authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Books.objects.filter(authors=self.object)
        return context


class AuthorCreateView(CreateView):
    model = Authors
    form_class = AuthorCreateForm


# EOF
