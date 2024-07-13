from django.db import models

# Create your models here.

class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=False,)
    location = models.CharField(max_length=255,default='NA')
    address = models.CharField(max_length=255)
    items = models.JSONField()
    def __str__(self):
        return f'{self.id} {self.name}'
   
