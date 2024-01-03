from django.urls import path, include
from rest_framework import routers

from . import views, api_views

router = routers.DefaultRouter()
router.register("books", api_views.BookViewSet)
router.register("authors", api_views.AuthorViewSet)
router.register("recipes", api_views.RecipeViewSet)
router.register("ingredients", api_views.IngredientViewSet)

app_name = "recipes"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/", include(router.urls)),
    path("search", views.search, name="search"),
    path(
        "books/", views.BooksListView.as_view(), name=views.BooksListView.list_view_name
    ),
    path(
        "books/<int:pk>",
        views.BooksDetailView.as_view(),
        name=views.BooksDetailView.detail_view_name,
    ),
    path(
        "authors/",
        views.AuthorsListView.as_view(),
        name=views.AuthorsListView.list_view_name,
    ),
    path(
        "authors/<int:pk>",
        views.AuthorsDetailView.as_view(),
        name=views.AuthorsDetailView.detail_view_name,
    ),
    path("authors/create", views.AuthorsCreateView.as_view(), name="authors_create"),
    path(
        "authors/<int:pk>/delete",
        views.AuthorsDeleteView.as_view(),
        name="authors_delete",
    ),
    path(
        "recipes/",
        views.RecipesListView.as_view(),
        name=views.RecipesListView.list_view_name,
    ),
    path(
        "recipes/<int:pk>",
        views.RecipesDetailView.as_view(),
        name=views.RecipesDetailView.detail_view_name,
    ),
    path(
        "ingredients/",
        views.IngredientsListView.as_view(),
        name=views.IngredientsListView.list_view_name,
    ),
    path(
        "ingredients/<int:pk>",
        views.IngredientsDetailView.as_view(),
        name=views.IngredientsDetailView.detail_view_name,
    ),
    path(
        "ingredients/create",
        views.IngredientsCreateView.as_view(),
        name="ingredients_create",
    ),
    path(
        "ingredients/<int:pk>/delete",
        views.IngredientsDeleteView.as_view(),
        name="ingredients_delete",
    ),
]
