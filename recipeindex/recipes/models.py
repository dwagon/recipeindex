""" Model Definition """
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    """Ingredients"""

    name = models.CharField(max_length=200)
    pantry = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Author(models.Model):
    """Authors"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """Books"""

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Recipes"""

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
