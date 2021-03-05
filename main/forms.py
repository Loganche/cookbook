from .models import Recipe, SignUp
from django.forms import ModelForm, TextInput, Textarea, PasswordInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe description'
            }),
        }


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = ["login", "password", "firstname", "lastname",]
        widgets = {
            "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Login'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            "firstname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
        }