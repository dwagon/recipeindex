
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("recipes/", include("recipes.urls", namespace="recipes")),
    path("admin/", admin.site.urls),
]
