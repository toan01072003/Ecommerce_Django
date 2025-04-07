from django.db import models

# Create your models here.
class Name(models.Model):
    family_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

class Address(models.Model):
    nation = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    office_code = models.CharField(max_length=20)
