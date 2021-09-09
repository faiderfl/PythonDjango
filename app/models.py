from django.db import models

# Create your models here.
class Country(models.Model):
    name= models.CharField(max_length=50)
    capital= models.CharField(max_length=50)
    area= models.IntegerField()