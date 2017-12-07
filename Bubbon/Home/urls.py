from django.conf.urls import url
from .import views




urlpatterns = [
    url(r'^$', views.Home, name='Home'),
    url(r'^(?P<saved_id>[0-9]+)/$', views.savedidM, name='savedidM'),
    url(r'^(?P<q>\w+)/$', views.LinkSearch, name = 'LinkSearch')
]
