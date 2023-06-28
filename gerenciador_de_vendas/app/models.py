from django.db import models



class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    ProductDescription = models.CharField(max_length=255)
    ProductPrice = models.FloatField(null=True)
    ProductStock = models.IntegerField(null=True)
    OtherDetails = models.CharField(max_length=255, null=True)
    ProductsCategory = models.CharField(max_length=255, null=True)



