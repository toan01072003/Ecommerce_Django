from django.db import models

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    item = models.ForeignKey('items.Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()