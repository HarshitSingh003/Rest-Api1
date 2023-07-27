from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Item,Company,Employee
from .serializers import ItemSerializer, CompanySerializer,EmployeeSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    

