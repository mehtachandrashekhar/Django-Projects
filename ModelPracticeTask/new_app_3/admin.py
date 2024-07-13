from django.contrib import admin
from .models import Student, Instructor,Course
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'Price', 'DOB', 'DOJ', 'Contact', 'Email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('Course_Title', 'Course_Code', 'Price', 'Desc', 'Start_Date', 'End_Date', 'is_available')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'Last_name', 'DOB', 'DOJ', 'Contact', 'Email', 'Department', 'is_available',
                    'linked_url')
