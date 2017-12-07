from django.db import models


class Member(models.Model):
    First_Name = models.CharField(max_length=16,default='Null')
    Last_Name = models.CharField(max_length=16,default='Null')
    username = models.CharField(max_length=16,primary_key=True)
    password = models.CharField(max_length=16)
    Address = models.CharField(max_length=16)
    PostCode = models.CharField(max_length=16,default='Null')
    Contact = models.CharField(max_length=10,default='Null')

    def __str__(self):
        return self.username





