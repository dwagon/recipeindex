from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("recipes/", include("recipes.urls", namespace="recipes")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
]
