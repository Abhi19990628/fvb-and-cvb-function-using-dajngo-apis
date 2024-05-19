from django.shortcuts import render
from rest_framework.views import APIView
from .models import Family
from .serailizers import FamilySerlizer
from rest_framework.response import Response




class FamilylistView (APIView):
    def get (self , request):
        familys=Family.objects.all()
        
