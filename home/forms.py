from django.db.models.base import Model
from django.forms import ModelForm, fields
from django.forms.models import model_to_dict
from home.models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person 
        fields = '__all__'