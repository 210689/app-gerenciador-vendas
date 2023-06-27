from django.db import models

class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    ProductDescription = models.CharField(max_length=255)

