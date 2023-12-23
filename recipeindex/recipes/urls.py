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
    path("recipe/<int:pk>", views.recipe, name="recipe"),
    path("ingredient/<int:pk>", views.ingredient, name="ingredient"),
    path("book/<int:pk>", views.book, name="book")
]
