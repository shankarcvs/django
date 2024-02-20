from django.db import models

# Create your models here.
class order(models.Model):
    item=models.CharField(max_length=100)
    price=models.IntegerField()
    place=models.TextField(max_length=200)
    paytype=models.TextField(max_length=100)
