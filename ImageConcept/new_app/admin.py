from django.contrib import admin

from .models import Book


# Register your models here.

class Showbook(admin.ModelAdmin):
    list_display = ('admin_photo', 'name', 'title', 'description', 'publish_date')


admin.site.register(Book, Showbook)
