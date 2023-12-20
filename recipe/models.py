""" Model Definition """
from django.db import models


# Create your models here.
class Ingredient(models.Model):
    """Ingredients"""

    name = models.CharField(max_length=200)
    pantry = models.BooleanField(default=False)


class Author(models.Model):
    """Authors"""

    name = models.CharField(max_length=200)


class Book(models.Model):
    """Books"""

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)


class Recipe(models.Model):
    """Recipes"""

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    book = models.ForeignKey(Book)
