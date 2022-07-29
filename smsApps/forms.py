from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from . models import Categorie
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'first_name':'First Name','last_name':'Last Name','email': 'Email'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            }


class CatForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['cat_name', 'cat_brand', 'active']
        labels = {'cat_name': 'Categorey name', 'cat_brand':'Brand' }
        widgets = {
            'cat_name':forms.TextInput(attrs={'class':'form-control'}),
            'cat_brand':forms.TextInput(attrs={'class':'form-control'}),
        }