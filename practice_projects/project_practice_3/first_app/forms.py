from django import forms
from django.forms.widgets import NumberInput
import datetime


FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class PracticeForm(forms.Form):
    name = forms.CharField(max_length=20,initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required = False,)
    agree = forms.BooleanField(label="Do you agree ?",)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}),initial=datetime.date.today)
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
