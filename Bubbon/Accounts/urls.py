from django.conf.urls import url
from Accounts.views import register, login, loggedin
import views



urlpatterns = [

    url(r'^register/$', register, name='register'),
    url(r'^$', login, name='login'),
    url(r'^logcheckuser/$', views.logCheckUser, name='logCheckUser'),





]
