from django.shortcuts import render

# Create your views here.
from .models import Provider, Publisher, Producer
from .serializers import ProviderSerializer, PublisherSerializer, ProducerSerializer
from rest_framework import viewsets
class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer