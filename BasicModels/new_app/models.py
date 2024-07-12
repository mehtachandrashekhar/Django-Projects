from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=40)
    Email = models.EmailField()
    Phone = models.BigIntegerField()
    TimeStamp = models.DateTimeField()
    Msg = models.TextField()
