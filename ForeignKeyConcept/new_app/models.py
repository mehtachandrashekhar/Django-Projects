from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=45)
    description = models.TextField()
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_name = models.CharField(max_length=35)
    product_desc = models.TextField()
    product_price = models.BigIntegerField()
    product_quantity = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
