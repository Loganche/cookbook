from .models import Recipe, Ingredient
from django.forms import ModelForm, TextInput, Textarea, PasswordInput, CheckboxInput


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "favourite"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Recipe description'
            }),
            "favourite": CheckboxInput(attrs={
                # 'placeholder': 'Favourite',
                # 'class': 'form-control'
            }),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingredient name'
            }),
        }

