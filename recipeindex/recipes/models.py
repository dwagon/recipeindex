""" Model Definition """
from django.db import models


# Create your models here.
class Ingredients(models.Model):
    """Ingredients"""

    name = models.CharField(max_length=200)
    pantry = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Authors(models.Model):
    """Authors"""

    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Books(models.Model):
    """Books"""

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Authors)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Recipes(models.Model):
    """Recipes"""

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredients)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        ordering = ["name"]

    def __str__(self):
        return self.name
