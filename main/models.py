from django.db import models

class Recipe(models.Model):
    title = models.CharField('Recipe Name', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.title #Shows text in Query output