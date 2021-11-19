from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(NationalPark)
admin.site.register(Attraction)
