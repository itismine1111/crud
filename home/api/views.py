from django.core.validators import validate_email
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.models import Person
from home.api.serializers import PersonSerializer
from home.api.auth_without_csrf import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication

class PersonView(APIView):

    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]

    def post(self, request):

        email = request.data.get("email")
        name = request.data.get("name")
        age = request.data.get("age")
        pk = request.data.get("pk")

        try:
            validate_email(email)
        except ValidationError:
            print("Email is not correct")

        # TODO: check if email already exists

        person = Person.objects.create(pk=pk, email=email, name=name, age=age)
        
        if person:
            person.save()

        return Response(status=status.HTTP_201_CREATED)


    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
