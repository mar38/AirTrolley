
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Home/', include('Home.urls')),
    url(r'^Accounts/', include('Accounts.urls')),
    url(r'^Basket/', include('Basket.urls')),
    url(r'^Search/', include('Search.urls')),
    url(r'^Checkout/', include('Checkout.urls', namespace='Checkout')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
