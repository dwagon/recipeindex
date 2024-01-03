from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
)
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


##################################################################################################################
class IngredientsListView(ListBreadcrumbMixin, ListView):
    model = Ingredients


class IngredientsDetailView(DetailView, DetailBreadcrumbMixin):
    model = Ingredients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(ingredients=self.object)
        return context


class IngredientsCreateView(CreateView):
    template_name = "recipes/ingredients_list.html"
    success_url = reverse_lazy("recipes:ingredients_list")
    model = Ingredients
    fields = ["name", "pantry"]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["object_list"] = Ingredients.objects.all()
        return data


class IngredientsDeleteView(DeleteView):
    model = Ingredients
    success_url = reverse_lazy("recipes:ingredients_list")


##################################################################################################################
class RecipesListView(ListBreadcrumbMixin, ListView):
    model = Recipes


class RecipesDetailView(DetailBreadcrumbMixin, DetailView):
    model = Recipes


##################################################################################################################


class BooksListView(ListBreadcrumbMixin, ListView):
    model = Books


class BooksDetailView(DetailBreadcrumbMixin, DetailView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(book=self.object)
        return context


##################################################################################################################


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


class AuthorsCreateView(CreateView):
    template_name = "recipes/authors_list.html"
    success_url = reverse_lazy("recipes:authors_list")
    model = Authors
    fields = ["name"]

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["object_list"] = Authors.objects.all()
        return data


class AuthorsDeleteView(DeleteView):
    model = Authors
    success_url = reverse_lazy("recipes:authors_list")


# EOF
