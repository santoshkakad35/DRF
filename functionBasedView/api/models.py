# models.py
from django.db import models

class Company_info(models.Model):
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.industry}"
