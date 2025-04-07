from django.db import models

# Create your models here.
class Book(models.Model):
    item = models.OneToOneField('items.Item', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey('admin_panel.Publisher', on_delete=models.SET_NULL, null=True)
        
    def display_title(self):
        return f"{self.title} by {self.author}"