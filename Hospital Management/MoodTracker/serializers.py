from rest_framework.serializers import ModelSerializer
from .models import *

class Employeeserializers(ModelSerializer):
    
    class Meta:
        model = information_db
        fields = "_all_" 