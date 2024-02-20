from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    mb_no=models.IntegerField(max_length=10)
    register_no=models.TextField()
    email=models.EmailField()
    pasout=models.FloatField()
