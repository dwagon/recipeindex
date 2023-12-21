from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SearchForm
from .models import Ingredient, Recipe, Book

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
    results = Ingredient.objects.filter(name__contains=name)
    print(f"DBG find_ingredients: {results=}")
    return results


def search_results(text: str):
    ingredients = find_ingredients(text)
    results = Recipe.objects.all()
    print(f"search_results {text=}")
    for ingredient in ingredients:
        print(f"search_results {ingredient=}")
        results = results.intersection(ingredient.recipe_set.all())
        print(f"search_results {results=}")

    return results

def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {"recipe": recipe}
    return render(request, "recipe.html", context)

def ingredient(request, pk):
    """ View an ingredient"""
    ingredient = Ingredient.objects.get(pk=pk)
    return render(request, "ingredient.html", {"ingredient": ingredient})

def book(request, pk):
    """ View a book"""
    book = Book.objects.get(pk=pk)
    recipes = Recipe.objects.filter(book=book)
    context = {"book": book, "recipes": recipes}
    return render(request, "book.html", context)
# EOF