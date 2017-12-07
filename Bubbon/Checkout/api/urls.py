from django.conf.urls import url
from django.contrib import admin

from .views import (CheckoutListAPIView, CheckoutPostSerializer)

app_name = "Search"

urlpatterns = [

    url(r'^$', CheckoutListAPIView.as_view(), name='Checkout'),
    url(r'^send/$', CheckoutPostSerializer.__base__, name='Checkout')

]
