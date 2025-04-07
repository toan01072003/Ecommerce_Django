from django.shortcuts import render

# Create your views here.
from .models import Staff
from .serializers import StaffSerializer
from rest_framework import viewsets
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer