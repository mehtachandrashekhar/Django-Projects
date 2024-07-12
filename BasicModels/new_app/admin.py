from django.contrib import admin
from .models import Contact


# Register your models here.

class ShowContact(admin.ModelAdmin):
    list_display = ['Name', 'Email', 'Phone', 'Msg', 'TimeStamp']


admin.site.register(Contact, ShowContact)
