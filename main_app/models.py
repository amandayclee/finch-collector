from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    habitat = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name