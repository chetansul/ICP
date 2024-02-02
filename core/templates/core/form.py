from django.forms import ModelForm
from core.models import  drugs


class appointment(ModelForm):
    class meta:
        model= drugs
        fields =["company" , "email","Productname", "state", "packmaterial","expirydate"]