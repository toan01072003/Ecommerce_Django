from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElectronicDeviceViewSet
router = DefaultRouter()
router.register(r'', ElectronicDeviceViewSet)
urlpatterns = [path('', include(router.urls))]