from django.conf.urls import url
from django.contrib import admin

from .views import (UserLoginAPIView)

app_name = "Search"

urlpatterns = [

    url(r'^$', UserLoginAPIView.as_view(), name='Login'),


]
