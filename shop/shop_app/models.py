from django.db import models

# Create your models here.

# Shop API model
class CartProduct(models.Model):
    product_name = models.CharField(max_length=256)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
