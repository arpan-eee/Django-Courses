from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        # fields = ["field_name",]
        # exclude = ["field_name",]
