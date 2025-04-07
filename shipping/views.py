from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Shipping
from .serializers import ShippingSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer