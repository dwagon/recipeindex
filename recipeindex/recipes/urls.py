from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
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
    path("books/create", views.BooksCreateView.as_view(), name="books_create"),
    path(
        "books/<int:pk>",
        views.BooksDetailView.as_view(),
        name=views.BooksDetailView.detail_view_name,
    ),
    path(
        "books/<int:pk>/delete",
        views.BooksDeleteView.as_view(),
        name="books_delete",
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
        "recipes/create/<int:book_id>",
        views.RecipesCreateBookView.as_view(),
        name="recipes_create_book",
    ),
    path("recipes/create", views.RecipesCreateView.as_view(), name="recipes_create"),
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
    path(
        r"ingredient-autocomplete/",
        views.IngredientAutocomplete.as_view(create_field="name"),
        name="ingredient-autocomplete",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(next_page=reverse_lazy("recipes:index")),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page=reverse_lazy("recipes:index")),
        name="logout",
    ),
]
