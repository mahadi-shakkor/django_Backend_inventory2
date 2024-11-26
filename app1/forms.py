from django import forms
from django import forms

from django import forms

class LoginForm(forms.Form):
    userid = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

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
        ('s', 'Supplier'),
        ('n', 'Neutroshonist'),
        ('w', 'Wirehouse Manager'),
        ('d', 'Distributor Company'),
        ('r', 'Reatailer')

    ]
    
# models.CharField(db_column='F', max_length=1, blank=True, null=True)  # Field name made lowercase.
#      models.CharField(db_column='S', max_length=1, blank=True, null=True)  # Field name made lowercase.
#      = models.CharField(db_column='N', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     = models.CharField(db_column='W', max_length=1, blank=True, null=True)  # Field name made lowercase.
#     = models.CharField(db_column='C', max_length=1, blank=True, null=True)  # Field name made lowercase.
#      = models.CharField(db_column='D', max_length=1, blank=True, null=True)  # Field name made lowercase.
#      = models.CharField(db_column='R', max_length=1, blank=True, null=True)  # Field name made lowercase.
#    

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
