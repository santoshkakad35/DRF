from django.contrib import admin
from .models import Company_info

# Register your models here.
@admin.register(Company_info)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name','industry')
    