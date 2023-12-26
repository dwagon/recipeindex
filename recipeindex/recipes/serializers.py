from rest_framework import serializers
from .models import Recipes, Books, Authors, Ingredients


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipes
        fields = ["url", "name", "ingredients", "book"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        depth = 0
        fields = ["url", "title", "authors"]


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(read_only=True, many=True, source="book_set")

    class Meta:
        model = Authors
        fields = ["url", "name", "books"]


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = ["url", "name", "pantry"]
