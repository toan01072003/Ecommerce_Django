from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    provider = models.ForeignKey('admin_panel.Provider', on_delete=models.SET_NULL, null=True)

    def is_in_stock(self):
        return self.stock > 0