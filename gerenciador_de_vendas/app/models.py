from django.db import models



class Products(models.Model):
    ProductName = models.CharField(max_length=255)
    ProductDescription = models.CharField(max_length=255)
    ProductPrice = models.FloatField(null=True)
    ProductStock = models.IntegerField(null=True)
    OtherDetails = models.CharField(max_length=255, null=True)
    ProductsCategory = models.CharField(max_length=255, null=True)


class Order(models.Model):
    requestDate = models.DateField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    status = models.CharField(max_length=10)
