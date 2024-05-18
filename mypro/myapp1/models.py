from django.db import models


class Family(models.Model):
    grandfather=models.CharField(max_length=20)
    grandmother=models.CharField(max_length=20)
    father=models.CharField(max_length=20)
    mother=models.CharField(max_length=20)
    brother=models.CharField(max_length=20)
    sister=models.CharField(max_length=20)
    family_member=models.CharField(max_length=10)