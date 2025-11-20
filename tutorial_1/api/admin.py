from django.contrib import admin
from .models import Student_info

# Register your models here.
@admin.register(Student_info)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','branch']