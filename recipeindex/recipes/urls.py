from django.urls import path, include
from rest_framework import routers

from . import views, api_views

router = routers.DefaultRouter()
router.register("books", api_views.BookViewSet)
router.register("authors", api_views.AuthorViewSet)
router.register("recipes", api_views.RecipeViewSet)
router.register("ingredients", api_views.IngredientViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
    path("search", views.search, name="search"),
    path("books/", views.BooksListView.as_view(), name="books_view"),
    path("books/<int:pk>", views.BooksDetailView.as_view(), name="books_detail"),
    path("authors/", views.AuthorsListView.as_view(), name="authors_view"),
    path("authors/<int:pk>", views.AuthorsDetailView.as_view(), name="authors_detail"),
    path("recipes/", views.RecipesListView.as_view(), name="recipes_view"),
    path("recipes/<int:pk>", views.RecipesDetailView.as_view(), name="recipes_detail"),
    path("ingredients/", views.IngredientsListView.as_view(), name="ingredients_view"),
    path("ingredients/<int:pk>", views.IngredientsDetailView.as_view(), name="ingredients_detail"),
]
