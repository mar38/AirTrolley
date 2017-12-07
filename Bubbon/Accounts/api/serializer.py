from django.forms import CharField
from mongoengine import ValidationError
from rest_framework.serializers import ModelSerializer
from Accounts.models import Member
from django.db.models import Q

class UserLoginSerializer(ModelSerializer):
    username = CharField(required=False)
    Password = CharField(required=False)
    class Meta:
        model = Member
        fields =  ('username', 'password' )

        def validate (self, data):
            username = data.get("username",None)
            Password = data.get("Password",None)
            if not username and Password:
                raise ValidationError("A username or password is not correct")

            return data

