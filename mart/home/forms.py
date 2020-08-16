from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "warranty_time_in_months",
            "manufacturing_date",
            "manufacturing_company",
            "company_contact_number",
            "company_email",
            "price",
            "total_numberof_products",
            "image_1",
            "image_2",
            "image_3",
            "image_4",
            "image_5",
        ]