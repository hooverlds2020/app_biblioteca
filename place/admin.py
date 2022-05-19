from django.contrib import admin
from .models import Sede, Rack, RackItem
# Register your models here.

admin.site.register(Sede)
admin.site.register(Rack)
admin.site.register(RackItem)