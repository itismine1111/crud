from django.shortcuts import redirect, render
from home.models import Person, Personx
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from home.api.serializers import PersonSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.forms import PersonForm

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        age = request.POST.get("age")
        pk = request.POST.get("pk")

        try:
            validate_email(email)
        except ValidationError:
            print("Email is not correct")

        # TODO: check if email already exists

        person = Person.objects.create(pk=pk, email=email, name=name, age=age)
        
        if person:
            person.save()

    elif request.method == "GET":
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return JsonResponse(serializer.data, status=201, safe=False)



def home2(request):
    if request.method == "POST":
        formdata = PersonForm(request.POST or None)

        if formdata.is_valid():
            formdata.save()
            return render(request, "home/home.html", {"form":PersonForm(), "message":"Posted Successfully"})

    else:
        form = PersonForm()
        return render(request, "home/home.html", {"form":form})
