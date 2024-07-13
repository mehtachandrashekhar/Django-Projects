from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ShowCategory(admin.ModelAdmin):
    list_display = ['cat_name']


admin.site.register(Category, ShowCategory)

class ShowProduct(admin.ModelAdmin):
    list_display = ['product_name', 'product_desc', 'product_price', 'product_quantity', 'category_id']
    list_per_page = 3
    list_filter = ['category_id', 'product_price']
    list_editable = ['product_quantity']
    search_fields = ['product_name', 'product_desc', 'category_id__cat_name']


admin.site.register(Product, ShowProduct)
