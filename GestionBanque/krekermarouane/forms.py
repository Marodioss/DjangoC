from dataclasses import field
from django.forms import ModelForm
from .models import Client
from .models import Compte
from .models import Operation

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class CompteForm(ModelForm):
    class Meta:
        model = Compte
        fields = '__all__'
        
class OperationForm(ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'