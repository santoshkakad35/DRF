from django.db import models

# Create your models here.
class Student_info(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    
    