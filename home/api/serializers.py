from django.db import models
from rest_framework import serializers
from home.models import Person

class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('id', 'email', 'name', 'age')
