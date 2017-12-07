from django.db import models
from django.core.urlresolvers import reverse

from Accounts.models import Member


class Rent(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, default='Null')
    numberofbedroom =models.IntegerField( default='Null')
    Description = models.CharField(max_length=100, default='Null')
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url (self):
        return reverse( kwargs={"id": self.id})

class Slides(models.Model):
        id = models.AutoField(primary_key=True)
        images = models.FileField(null=True, blank=True)

        def get_absolute_url(self):
            return reverse(kwargs={"id": self.id})

class Product (models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    type = models.CharField(max_length=100, default='Null')
    Description = models.CharField(max_length=100, default='Null')
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.FileField(null=True, blank=True)

    def __unicode__(self):
        return self.type

    def get_absolute_url (self):

        return reverse( kwargs={"id": self.id})

class SavedItems(models.Model):
    Userid =  models.CharField(max_length=100, default='Null')
    Display_id =  models.IntegerField( default='Null')

    def __int__(self):
        return self.id
