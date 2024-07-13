from django.db import models

# Create your models here.

Course_list = [
    ('python', 'Python'),
    ('react', 'React'),
    ('flutter', 'Flutter'),
    ('django', 'Django'),
    ('php', 'Php')
]

Department_list = [
    ('sales', 'Sales'),
    ('marketing', 'Marketing'),
    ('teaching', 'Teaching'),
    ('development', 'Development')
]

class Student(models.Model):
    First_name = models.CharField(max_length=45, verbose_name='First name')
    Last_name = models.CharField(max_length=45, verbose_name='Last name')
    Price = models.IntegerField()
    DOB = models.DateField(verbose_name='Date of Birth')
    DOJ = models.DateField(auto_now=True, verbose_name='Date of Joining')
    Contact = models.BigIntegerField()
    Email = models.EmailField()

class Course(models.Model):
    Course_Title = models.CharField(max_length=45, choices=Course_list)
    Course_Code = models.IntegerField()
    Price = models.IntegerField()
    Desc = models.TextField()
    Start_Date = models.DateField(auto_now=True)
    End_Date = models.DateField()
    is_available = models.BooleanField( default=True, verbose_name='Active Status')

class Instructor(models.Model):
    First_name = models.CharField(max_length=45, verbose_name='First name')
    Last_name = models.CharField(max_length=45, verbose_name='Last name')
    DOB = models.DateField(verbose_name='Date of Birth')
    DOJ = models.DateField(auto_now=True, verbose_name='Date of Joining')
    Contact = models.BigIntegerField()
    Email = models.EmailField()
    Department = models.CharField(max_length=40, choices=Department_list)
    is_available = models.BooleanField(default=True, verbose_name='Active Status')
    linked_url = models.URLField()