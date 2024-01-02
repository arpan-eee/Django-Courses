from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        # fields = ["field_name",]
        # exclude = ["field_name",]
