from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FamilySerializer
from .models import Family
from rest_framework import status

@api_view(['GET', 'POST'])
def FamilyListView(request):
    if request.method == 'GET':
        familys = Family.objects.all()
        familys_serializer = FamilySerializer(familys, many=True)
        return Response(familys_serializer.data)
    
    elif request.method == 'POST':
        familys_serializer = FamilySerializer(data=request.data)
        if familys_serializer.is_valid():
            familys_serializer.save()
            return Response(familys_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(familys_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def FamilyDetailsView(request, pk):
    familys = get_object_or_404(Family, pk=pk)
    
    if request.method == 'GET':
        familys_serializer = FamilySerializer(familys)
        return Response(familys_serializer.data)
    
    elif request.method == 'PUT':
        familys_serializer = FamilySerializer(familys, data=request.data)
        if familys_serializer.is_valid():
            familys_serializer.save()
            return Response(familys_serializer.data)
        return Response(familys_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        familys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
