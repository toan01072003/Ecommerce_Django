from django.db import models

# Create your models here.
from django.db import models
from shared.models import Name, Address

class Customer(models.Model):
    name = models.OneToOneField(Name, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def get_full_name(self):
        return f"{self.name.family_name} {self.name.last_name} {self.name.name}"