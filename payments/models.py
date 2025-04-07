from django.db import models

# Create your models here.
class Payment(models.Model):
    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100)
    
    
    def is_successful(self):
        return self.status.lower() == "success"