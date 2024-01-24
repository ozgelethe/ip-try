from django.db import models

# Create your models here.

class IPAddress(models.Model):
    address = models.CharField(max_length=100)
    otx_info = models.TextField(blank=True)
    
    objects = models.Manager()