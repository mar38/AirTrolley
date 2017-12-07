from django.contrib import admin

from .models import *

from .models import Rent

admin.site.register(Rent)
admin.site.register(Slides)
admin.site.register(Product)
admin.site.register(SavedItems)
