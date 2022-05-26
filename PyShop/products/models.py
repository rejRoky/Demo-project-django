from django.db import models

# Create your models here.


class Product (models.Model):
    pName = models.CharField(max_length=255)
    pPrice = models.FloatField()
    pStock = models.IntegerField()
    pImage_url = models.CharField(max_length=2083)


class Offer(models.Model):
    pCode = models.CharField(max_length=10)
    pDescription = models.CharField(max_length=255)
    pDiscount = models.FloatField()
