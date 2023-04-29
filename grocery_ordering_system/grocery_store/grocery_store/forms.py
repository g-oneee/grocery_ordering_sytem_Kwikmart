from django import forms
from app.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'price', 'stock' ,'threshold_value', 'category' , 'sub_category' ,'brand' ]

# class OrderForm(forms.ModelForm):

#     class Meta:
#         model = Order
#         # fields = ['_all_']