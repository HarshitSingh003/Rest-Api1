from rest_framework import serializers
from .models import Item, Company,Employee

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        #fields = ('id', 'name', 'description', 'price')
        field="__all__"
        
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"