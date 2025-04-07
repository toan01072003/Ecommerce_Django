from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Provider, Publisher, Producer
admin.site.register(Provider)
admin.site.register(Publisher)
admin.site.register(Producer)