from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ---- customers/urls.py ----
from .views import CustomerViewSet
router = DefaultRouter()
router.register(r'', CustomerViewSet)
urlpatterns = [path('', include(router.urls))]