from rest_framework import serializers
from .models import Family
 
 
class FamilySerlizer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'  
