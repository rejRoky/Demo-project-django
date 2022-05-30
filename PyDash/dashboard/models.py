from django.db import models


class Summary (models.Model):
    pSKU = models.CharField(max_length=255)
    pName = models.CharField(max_length=255)
    pPrice = models.FloatField()
    pStock = models.IntegerField()


class Dashboard (models.Model):
    dispenseInfo = models.CharField(max_length=255)
    saleInfo = models.CharField(max_length=255)
    deviceInfo = models.CharField(max_length=255)
    userInfo = models.CharField(max_length=255)
    rfidInfo = models.IntegerField()


class Complain (models.Model):
    complainLog = models.CharField(max_length=2083)
    saleInfo = models.CharField(max_length=255)


