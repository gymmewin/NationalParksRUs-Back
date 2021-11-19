from django.db import models

# Create your models here.

class NationalPark(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    admission_fee = models.FloatField()


    class Meta:
        verbose_name = 'national_park'
        verbose_name_plural = verbose_name

class Attraction(models.Model):
    attraction_name = models.CharField(max_length=180)
    park = models.ForeignKey(NationalPark, related_name='top_attractions', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
