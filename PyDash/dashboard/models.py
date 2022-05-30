from django.db import models


class Dashboard (models.Model):
    dispenseInfo = models.CharField(max_length=255)
    saleInfo = models.CharField(max_length=255)
    deviceInfo = models.CharField(max_length=255)
    userInfo = models.CharField(max_length=255)
    rfidInfo = models.IntegerField()
