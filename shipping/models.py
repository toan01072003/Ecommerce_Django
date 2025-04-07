from django.db import models

# Create your models here.
class Shipping(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    address = models.OneToOneField('shared.Address', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=100)

    def is_delivered(self):
        return self.status.lower() == "delivered"