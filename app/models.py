from django.db import models

# Create your models here.
class resume(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)
    summary=models.TextField(max_length=200)
    degree=models.CharField(max_length=200)
    university=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    pervious=models.TextField(max_length=2000)
    skills=models.TextField(max_length=200)

