from django.db import models

class Offers(models.Model):
    title = models.CharField(max_length = 100)
    details = models.CharField(max_length = 255)
    icon = models.ImageField(upload_to='images/')

class Goods(models.Model):
    details = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='images/')
