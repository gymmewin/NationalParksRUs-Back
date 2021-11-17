from django.db import models

# Create your models here.

class NationalPark(models.Model):
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    admission_fee = models.FloatField()
