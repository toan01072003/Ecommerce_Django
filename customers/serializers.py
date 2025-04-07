from rest_framework import serializers

# ---- customers/serializers.py ----
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'