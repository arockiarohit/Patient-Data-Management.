from django.forms import ModelForm
from .models import *

class DataForm(ModelForm):
    class Meta:
        model = information_db
        fields = "__all__"

class DataForm1(ModelForm):
    class Meta:
        model = Patient_db
        fields = "__all__"
