import string
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    DeleteView,
)
from dal import autocomplete
from view_breadcrumbs import (
    DetailBreadcrumbMixin,
    ListBreadcrumbMixin,
    BaseBreadcrumbMixin,
)
from .forms import (
    SearchForm,
    AuthorCreateForm,
    BooksCreateForm,
    RecipesCreateForm,
    RecipesCreateBookForm,
)
from .models import Ingredients, Recipes, Books, Authors


##################################################################################################################
class IndexView(BaseBreadcrumbMixin, TemplateView):
    template_name = "index.html"
    crumbs = []


##################################################################################################################
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
        data = super().get_context_data(**kwargs)
        data["recipes"] = Recipes.objects.filter(ingredients=self.object)
        data["recipe"] = {}
        for letter in string.ascii_uppercase:
            if recipes := Recipes.objects.filter(
                name__startswith=letter, ingredients=self.object
            ):
                data["recipe"][letter] = list(recipes)
        return data


class IngredientsCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipes/ingredients_list.html"
    success_url = reverse_lazy("recipes:ingredients_list")
    model = Ingredients
    fields = ["name", "pantry"]
    login_url = reverse_lazy("recipes:login")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["object_list"] = Ingredients.objects.all()
        return data


class IngredientsDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredients
    success_url = reverse_lazy("recipes:ingredients_list")
    login_url = reverse_lazy("recipes:login")


class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Ingredients.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


##################################################################################################################
class RecipesListView(ListBreadcrumbMixin, ListView):
    model = Recipes

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["recipe"] = {}
        for letter in string.ascii_uppercase:
            if recipes := Recipes.objects.filter(name__startswith=letter):
                data["recipe"][letter] = list(recipes)
        return data


class RecipesDetailView(DetailBreadcrumbMixin, DetailView):
    model = Recipes


class RecipesCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipes/recipes_create.html"
    success_url = reverse_lazy("recipes:recipes_list")
    form_class = RecipesCreateForm
    model = Recipes
    login_url = reverse_lazy("recipes:login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["media"] = autocomplete.Select2.media
        return context

    def get_success_url(self):
        return reverse_lazy(f"recipes:books_detail", args=[self.object.book.id])


class RecipesCreateBookView(RecipesCreateView):
    """Create a recipe with the book already specified"""

    form_class = RecipesCreateBookForm

    def get_initial(self):
        return {"book": self.kwargs.get("book_id")}


##################################################################################################################
class BooksListView(ListBreadcrumbMixin, ListView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["authors"] = Authors.objects.all()
        return context


class BooksDetailView(DetailBreadcrumbMixin, DetailView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(book=self.object)
        context["recipe"] = {}
        for letter in string.ascii_uppercase:
            if recipes := Recipes.objects.filter(
                book=self.object, name__startswith=letter
            ):
                context["recipe"][letter] = list(recipes)
        return context


class BooksCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipes/books_create.html"
    success_url = reverse_lazy("recipes:books_list")
    form = BooksCreateForm
    model = Books
    fields = ["title", "authors"]
    login_url = reverse_lazy("recipes:login")


class BooksDeleteView(LoginRequiredMixin, DeleteView):
    model = Books
    success_url = reverse_lazy("recipes:books_list")
    login_url = reverse_lazy("recipes:login")


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


class AuthorsCreateView(LoginRequiredMixin, CreateView):
    template_name = "recipes/authors_list.html"
    success_url = reverse_lazy("recipes:authors_list")
    model = Authors
    fields = ["name"]
    login_url = reverse_lazy("recipes:login")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["object_list"] = Authors.objects.all()
        return data


class AuthorsDeleteView(LoginRequiredMixin, DeleteView):
    model = Authors
    success_url = reverse_lazy("recipes:authors_list")
    login_url = reverse_lazy("recipes:login")


# EOF
