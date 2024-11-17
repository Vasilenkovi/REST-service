from django.db import models


class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    address = models.CharField(max_length=60)