from rest_framework.serializers import ModelSerializer
from Checkout.models import Checkout

class CheckoutSerializer(ModelSerializer):
    class Meta:
        model = Checkout
        fields =  ('FirstName', 'LastName','Address','City','PostCode','number','Email' )

class   CheckoutPostSerializer(ModelSerializer):
    class Meta:
        model = Checkout
        fields = ('FirstName', 'LastName','Address','City','PostCode','number','Email' )

