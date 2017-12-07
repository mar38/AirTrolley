from rest_framework.generics import ListAPIView, RetrieveAPIView
from Checkout.models import Checkout
from django.db.models import Q
from .serializer import CheckoutSerializer,CheckoutPostSerializer
from rest_framework.filters import SearchFilter



class CheckoutListAPIView (ListAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer


class PostDetailAPIView (RetrieveAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutPostSerializer
