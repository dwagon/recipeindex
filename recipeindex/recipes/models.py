""" Model Definition """
from django.db import models


# Create your models here.
class Ingredients(models.Model):
    """Ingredients"""

    name = models.CharField(max_length=200)
    pantry = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Authors(models.Model):
    """Authors"""

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Books(models.Model):
    """Books"""

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Authors)

    def __str__(self):
        return self.title


class Recipes(models.Model):
    """Recipes"""

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredients)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
