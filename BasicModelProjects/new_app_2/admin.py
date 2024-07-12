from django.contrib import admin
from .models import Supplier, Warehouse, Product
# Register your models here.

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Phone', 'Email', 'Website', 'is_Active')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Category', 'Price', 'Quantity', 'Timestamp')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Capacity', 'Manager', 'Contact')