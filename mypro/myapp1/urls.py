from django.urls import path
from .views import FamilyListView, FamilyDetailsView

urlpatterns = [
    path('familys/', FamilyListView),
    path('familys/<int:pk>/', FamilyDetailsView)
]
