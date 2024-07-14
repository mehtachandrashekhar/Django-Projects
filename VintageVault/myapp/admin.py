from django.contrib import admin

from .models import Country, State, City, UserProfile, ItemCategory, Item, ProductCart, Order, Payment, Feedback, ContactUs
# admin.py

from django.contrib import admin
from unfold.admin import ModelAdmin

# Register your models here.


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(ItemCategory)
admin.site.register(Item)
admin.site.register(ProductCart)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(ContactUs)
