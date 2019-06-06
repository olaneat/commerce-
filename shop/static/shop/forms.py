from django.form import forms
from .models import Product

class ProductForm(forms.ModelForm):
    def clean_price(self):
        if self.cleaned_data['price'] <=0:
            raise forms.ValidationError("enter a valid price")
        return.self.cleaned_data['price']
        
