from rest_framework import serializers
from .models import Worker

class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'first_name', 
            'middle_name', 
            'last_name', 
            'position', 
            'is_active'
        ]

class WorkerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        worker = Worker.objects.create(**validated_data)
        return worker