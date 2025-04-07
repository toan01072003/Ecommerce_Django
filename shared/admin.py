from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Name, Address
admin.site.register(Name)
admin.site.register(Address)