from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .forms import SearchForm
from .models import Ingredients, Recipes, Books, Authors

def index(request):
    return render(request, "index.html")

def search(request):
    """ Find a recipe with ingredients"""
    results = {}
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            results = search_results(form.cleaned_data['text'])
    else:
        form = SearchForm()

    context = {"form": form, "results": results}
    return render(request, "search.html", context)

def find_ingredients(name: str):
    """ Find an ingredient by name"""
    results = Ingredients.objects.filter(name__contains=name)
    print(f"DBG find_ingredients: {results=}")
    return results


def search_results(text: str):
    ingredients = find_ingredients(text)
    results = Recipes.objects.all()
    print(f"search_results {text=}")
    for ingredient in ingredients:
        print(f"search_results {ingredient=}")
        results = results.intersection(ingredient.recipes_set.all())
        print(f"search_results {results=}")

    return results

class IngredientsListView(ListView):
    model = Ingredients

class IngredientsDetailView(DetailView):
    model = Ingredients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(ingredients=self.object)
        return context

class RecipesListView(ListView):
    model = Recipes

class RecipesDetailView(DetailView):
    model = Recipes

class BooksListView(ListView):
    model = Books

class BooksDetailView(DetailView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipes"] = Recipes.objects.filter(book=self.object)
        return context

class AuthorsListView(ListView):
    model = Authors

class AuthorsDetailView(DetailView):
    model = Authors

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Books.objects.filter(authors=self.object)
        return context

# EOF