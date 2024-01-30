from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm



class regform(forms.Form):
    first_name=forms.CharField(min_length=4,max_length=15)
    last_name=forms.CharField(min_length=4,max_length=15)
    age=forms.IntegerField()
    adress=forms.CharField(max_length=15)
    emailid=forms.EmailField()
    phone=forms.IntegerField()
    password=forms.CharField(min_length=8,max_length=15,widget=forms.PasswordInput)
    confirm_password=forms.CharField(min_length=8,max_length=15,widget=forms.PasswordInput)



class LoginForm(forms.Form):
    emailid  = forms.EmailField()
    password = forms.CharField(min_length=8,max_length=15,widget=forms.PasswordInput)

