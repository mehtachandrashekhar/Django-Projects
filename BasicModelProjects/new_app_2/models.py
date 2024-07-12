from django.db import models

# Create your models here.
category_list = [
    ("cloth", "Cloth"),
    ("electronics", "Electronics"),
    ("digital", "Digital"),
    ("stationery", "Stationery")
]

capacity_list = [
    ("small", "Small"),
    ("medium", "Medium"),
    ("large", "Large"),
    ("extra_large", "Extra_large")
]

class Product(models.Model):
    Category = models.CharField(max_length=40, choices=category_list)
    Name = models.CharField(max_length=40)
    Desc = models.TextField()
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Timestamp = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    Name = models.CharField(max_length=40, verbose_name="Name")
    Phone = models.BigIntegerField()
    Email = models.EmailField()
    Address = models.TextField()
    Website = models.URLField()
    is_Active = models.BooleanField(default=True, verbose_name="Active Status")

class Warehouse(models.Model):
    Name = models.CharField(max_length=40)
    Address = models.TextField()
    Capacity = models.CharField(max_length=30, choices=capacity_list)
    Manager = models.CharField(max_length=40)
    Contact = models.BigIntegerField()
