from rest_framework import serializers
from .models import ESP

class EspSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESP
        # fileds = ('name','mode') 
        fields = '__all__'