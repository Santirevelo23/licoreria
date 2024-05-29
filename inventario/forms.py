from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'azure_image_url']
        labels = {
            'name': 'Nombre',
            'price': 'Precio',
            'azure_image_url': 'Azure Blob Storage Image URL',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Nombre'}),
            'price': forms.TextInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Precio'}),
            'azure_image_url': forms.URLInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Enter Azure Blob Storage image URL'}),
        }
