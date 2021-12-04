from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EspSerializer
from esp32.models import ESP
# Create your views here.
# esp32/
class EspList(APIView):
    serializer_class = EspSerializer
    def get (self,request):
        # esp_name= request.query_params.get([id])
        id = request.query_params["name"]
        
        if id!=None:
            esp = ESP.objects.get(name = id)
            esp_serializer = self.serializer_class(esp)
        else:
            esp = ESP.objects.all()
            esp_serializer = self.serializer_class(esp,many=True)
        return Response(esp_serializer.data,status=status.HTTP_200_OK)
    #    if not esp_list:
    #         return Response({'message':'no esp found'})
        # esp_list = ESP.objects.all()
       
        
    def post(self, request):
        pass