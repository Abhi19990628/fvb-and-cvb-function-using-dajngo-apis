from django.db import models

class Family(models.Model):
    FamilyName=models.CharField(max_length=20)
    GrandFather=models.CharField(max_length=20)
    GandMother=models.CharField(max_length=20)
    Mother=models.CharField(max_length=20)
    Father=models.CharField(max_length=20)
    Brother=models.CharField(max_length=20)
    Sister=models.CharField(max_length=20)
    family_size=models.IntegerField()