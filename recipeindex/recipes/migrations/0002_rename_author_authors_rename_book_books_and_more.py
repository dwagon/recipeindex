# Generated by Django 5.0 on 2023-12-23 01:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Author",
            new_name="Authors",
        ),
        migrations.RenameModel(
            old_name="Book",
            new_name="Books",
        ),
        migrations.RenameModel(
            old_name="Ingredient",
            new_name="Ingredients",
        ),
        migrations.RenameModel(
            old_name="Recipe",
            new_name="Recipes",
        ),
    ]
