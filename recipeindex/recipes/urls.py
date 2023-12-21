from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("recipe/<int:pk>", views.recipe, name="recipe"),
    path("ingredient/<int:pk>", views.ingredient, name="ingredient")
]