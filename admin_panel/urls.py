
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, PublisherViewSet, ProducerViewSet
router = DefaultRouter()
router.register(r'providers', ProviderViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'producers', ProducerViewSet)
urlpatterns = [path('', include(router.urls))]