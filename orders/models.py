from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    
    def is_completed(self):
        return self.status.lower() == "completed"

    def get_item_count(self):
        return self.cart_set.count()