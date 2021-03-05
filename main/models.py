from django.db import models


class Recipe(models.Model):
    title = models.CharField('Recipe Name', max_length=50)
    description = models.TextField('Description')
    favourite = models.BooleanField('Favourite', default=False)

    def __str__(self):
        return self.title  # Shows text in Query output


class SignUp(models.Model):
    login = models.CharField('Login', max_length=50)
    password = models.CharField('Password', max_length=50)
    firstname = models.CharField('First Name', max_length=50)
    lastname = models.CharField('Last Name', max_length=50)

    def __str__(self):
        return self.login
