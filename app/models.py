from time import time
from django.db import models

# Create your models here.
class Details(models.Model):
    username = models.CharField(max_length=100)
    email=models.EmailField()
    city = models.CharField(max_length=100)
    time = models.TimeField()
    