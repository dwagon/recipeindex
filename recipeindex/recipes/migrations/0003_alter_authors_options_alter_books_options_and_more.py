# Generated by Django 5.0 on 2023-12-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_rename_author_authors_rename_book_books_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="authors",
            options={
                "ordering": ["name"],
                "verbose_name": "Author",
                "verbose_name_plural": "Authors",
            },
        ),
        migrations.AlterModelOptions(
            name="books",
            options={
                "ordering": ["title"],
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
        migrations.AlterModelOptions(
            name="ingredients",
            options={
                "ordering": ["name"],
                "verbose_name": "Ingredient",
                "verbose_name_plural": "Ingredients",
            },
        ),
        migrations.AlterModelOptions(
            name="recipes",
            options={
                "ordering": ["name"],
                "verbose_name": "Recipe",
                "verbose_name_plural": "Recipes",
            },
        ),
        migrations.AlterField(
            model_name="authors",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="books",
            name="authors",
            field=models.ManyToManyField(blank=True, to="recipes.authors"),
        ),
        migrations.AlterField(
            model_name="books",
            name="title",
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name="ingredients",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]