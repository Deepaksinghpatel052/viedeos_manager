from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  VsUsers
CHOICES=[('Perfomer','I AM A PERFOMER'),('Voter','I am a Voter')]
class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Username"}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Password"}))
    password2 = forms.CharField(required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={"class": "form-control","placeholder": "Confirm Password"}))
    email = forms.EmailField(max_length=254, help_text='Email.',widget=forms.TextInput(attrs={"class": "form-control","placeholder": "E-mail"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class  VsUsersForm(forms.ModelForm):

    Type = forms.CharField(label='Type', widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Name"}))
    Contact_no = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "Phone No","id":"phone2"}))
    Zip_Code = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "Zipcode"}))
    class Meta:
        model = VsUsers
        fields = ('name', 'Contact_no','Type', 'Zip_Code', )


