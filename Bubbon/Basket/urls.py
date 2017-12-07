from django.conf.urls import url
from .import views

from django.conf import settings



urlpatterns = [

    url(r'^$', views.Basket, name='Basket'),
    url(r'^(?P<Display_id>[0-9]+)/$', views.remove, name='remove'),



]
