from django.db import models


class Ingredient(models.Model):
    # Recipe-Ingredient M-M in Recipe

    name = models.CharField('Ingredient Name', max_length=50, default="Default Ingredient", null=True)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    # Recipe-Ingredient M-M
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, default="Default Ingredient", null=True)

    title = models.CharField('Recipe Name', max_length=50, default="Default Title", null=True)
    description = models.TextField('Description', default="Default Description", null=True)
    favourite = models.BooleanField('Favourite', default=False, null=True)

    def __str__(self):
        return self.title  # Shows text in Query output

