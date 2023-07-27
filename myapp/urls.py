from django.contrib import admin
# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet,CompanyViewSet,EmployeeViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'companies',CompanyViewSet)
router.register(r'employee',EmployeeViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
