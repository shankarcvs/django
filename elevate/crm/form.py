from django import forms
from rest_framework import serializers
from .models import student

class StudentForm(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'