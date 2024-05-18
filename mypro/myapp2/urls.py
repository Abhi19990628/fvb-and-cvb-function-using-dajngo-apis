from django.urls import path
from .views import APIView

urlpatterns = [
    path('familyss',APIView.as_view())   
]
