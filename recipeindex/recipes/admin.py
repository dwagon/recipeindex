from django.contrib import admin

from .models import Ingredients, Books, Authors, Recipes

admin.site.register(Ingredients)
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Recipes)
