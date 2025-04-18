"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),

    # Microservice API endpoints
    path('api/customers/', include('customers.urls')),
    path('api/items/', include('items.urls')),
    path('api/books/', include('books.urls')),
    path('api/devices/', include('electronics.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/shipping/', include('shipping.urls')),
    path('api/staff/', include('staff.urls')),
    path('api/admin-panel/', include('admin_panel.urls')),
]
