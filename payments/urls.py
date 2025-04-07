
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet
router = DefaultRouter()
router.register(r'', PaymentViewSet)
urlpatterns = [path('', include(router.urls))]