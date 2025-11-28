from django import forms
from .models import Categorie

class CrearCategorie(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name',"description"]