from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class Checkout(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    PostCode = models.CharField(max_length=50)
    number =models.IntegerField(default=5)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.FirstName

    def __str__(self):
        return self.LastName


    def __str__(self):
        return self.Address

    def __str__(self):
        return self.City

    def __str__(self):
        return self.Postcode

    def __str__(self):
        return self.Email
    def __int__(self):
        return self.PhoneNumber




