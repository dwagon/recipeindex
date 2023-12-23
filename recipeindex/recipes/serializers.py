from rest_framework import serializers
from .models import Recipe, Book, Author, Ingredient

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ["url", "name", "ingredients", "book"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        depth = 0
        fields = ["url", "title", "authors"]



class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(read_only=True, many=True, source="book_set")
    class Meta:
        model = Author
        fields = ["url", "name", "books"]



class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["url", "name", "pantry"]

