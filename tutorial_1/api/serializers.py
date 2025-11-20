from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    branch = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        from .models import Student_info
        return Student_info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.branch = validated_data.get('branch', instance.branch)
        instance.save()
        return instance