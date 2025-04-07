from django.shortcuts import render

# Create your views here.
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer