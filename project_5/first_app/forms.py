from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    email = forms.EmailField(label = "User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    age = forms.CharField(widget=forms.NumberInput)
    check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    MEAL = [('P', 'Pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)