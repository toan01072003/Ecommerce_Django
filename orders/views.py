from django.shortcuts import render

# Create your views here.
from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer