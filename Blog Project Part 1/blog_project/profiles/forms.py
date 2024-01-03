from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        # fields = ["field_name",]
        # exclude = ["field_name",]
