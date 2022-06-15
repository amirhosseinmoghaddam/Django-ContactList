from dataclasses import fields
from pyexpat import model
from .models import Contact
from django import forms
from django.contrib.auth.models import User

class AddContactForm(forms.ModelForm):
    username = User.username
    firstname = forms.CharField(max_length=150)
    lastname = forms.CharField(max_length=150)
    tel_type = forms.CharField(max_length=100)
    number = forms.IntegerField()

    class Meta:
        model = Contact
        fields = ("__all__")
