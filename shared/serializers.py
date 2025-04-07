from .models import Name, Address
from rest_framework import serializers
class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'