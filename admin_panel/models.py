from django.db import models

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField('shared.Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    def full_address(self):
            addr = self.address
            return f"{addr.street} {addr.house_number}, {addr.city}, {addr.nation}"

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField('shared.Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    def full_address(self):
            addr = self.address
            return f"{addr.street} {addr.house_number}, {addr.city}, {addr.nation}"

class Producer(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField('shared.Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    def full_address(self):
            addr = self.address
            return f"{addr.street} {addr.house_number}, {addr.city}, {addr.nation}"