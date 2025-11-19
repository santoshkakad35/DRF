# serializers.py
from rest_framework import serializers
from .models import Company_info

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company_info
        fields = '__all__'   # ✅ include all fields from the Company model
