from django import forms
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
    Users_Type = [
        ('', 'Select a User Type'),  # This will be the default option, with an empty value
        ('a', 'Aggricultural Officer'),
        ('f', 'Farmer'),
        ('c', 'Customer'),
    ]
    
    Choosed_User_Type= forms.ChoiceField(
        choices=Users_Type,
        required=True,
        label=" User Type "
    )
    street = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Street'}))
    city = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    country = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    postalcode = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Postal Code'}))
