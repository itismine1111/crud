from django.shortcuts import render
from home.models import Person
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from home.api.serializers import PersonSerializer
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        age = request.POST.get("age")

        try:
            validate_email(email)
        except ValidationError:
            print("Email is not correct")

        # TODO: check if email already exists

        person = Person.objects.create(email=email, name=name, age=age)
        
        if person:
            person.save()

    elif request.method == "GET":
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)