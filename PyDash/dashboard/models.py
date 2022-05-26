from django.db import models


class Summary (models.Model):
    pSKU = models.CharField(max_length=255)
    pName = models.CharField(max_length=255)
    pPrice = models.FloatField()
    pStock = models.IntegerField()



