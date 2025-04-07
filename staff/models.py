from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.OneToOneField('shared.Name', on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # e.g., 'order', 'delivery'
    contact = models.CharField(max_length=50)
    
    
    def get_display_name(self):
        return f"{self.name.family_name} {self.name.name} ({self.role})"