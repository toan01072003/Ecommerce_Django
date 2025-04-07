from django.shortcuts import render

# Create your views here.
from .models import Cart
from .serializers import CartSerializer
from rest_framework import viewsets
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_total_price(self):
        return self.item.price * self.quantity