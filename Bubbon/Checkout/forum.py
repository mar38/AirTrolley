from django.contrib.auth.models import User
from django import forms
from models import Checkout



class CheckoutForm (forms.ModelForm):
    FirstName = forms.CharField(max_length=100)
    LastName = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=1000)
    City = forms.CharField(max_length=100)
    PostCode = forms.CharField(max_length=10)
    number = forms.IntegerField()
    Email = forms.EmailField(max_length=100)
    class Meta:
        model = Checkout
        fields = ["FirstName", "LastName","Address", "City","PostCode","number","Email" ]
