from django.db import models

# Create your models here.
class ElectronicDevice(models.Model):
    item = models.OneToOneField('items.Item', on_delete=models.CASCADE)
    specs = models.TextField()
    warranty_period = models.CharField(max_length=50)
    producer = models.ForeignKey('admin_panel.Producer', on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey('admin_panel.Provider', on_delete=models.SET_NULL, null=True)
    
    def get_provider_name(self):
        return self.provider.name if self.provider else "Unknown"

    def get_producer_name(self):
        return self.producer.name if self.producer else "Unknown"