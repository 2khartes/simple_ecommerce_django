from django import forms
from .models import Product

class CrearProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name',"description","img","price","stock" ]