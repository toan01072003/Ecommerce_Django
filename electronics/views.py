from django.shortcuts import render

# Create your views here.
from .models import ElectronicDevice
from .serializers import ElectronicDeviceSerializer
from rest_framework import viewsets
class ElectronicDeviceViewSet(viewsets.ModelViewSet):
    queryset = ElectronicDevice.objects.all()
    serializer_class = ElectronicDeviceSerializer