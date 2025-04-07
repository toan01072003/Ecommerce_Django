
from .models import ElectronicDevice
from rest_framework import serializers
class ElectronicDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicDevice
        fields = '__all__'