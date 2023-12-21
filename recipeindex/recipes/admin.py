from django.contrib import admin

from .models import Ingredient, Book, Author, Recipe

admin.site.register(Ingredient)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Recipe)