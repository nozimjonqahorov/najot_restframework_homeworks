from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from .models import Moto
from .serializers import MotoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class MotoListCreateView(ListCreateAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response({
            "status":status.HTTP_200_OK,
            "soni":queryset.count(),
            "message":"Barcha mototsikllar ro'yxati", 
            "data": serializer.data
        })
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            "status":status.HTTP_201_CREATED,
            "message":"Yangi mototsikl qo'shildi", 
            "data": serializer.data
        })
    


class MotoDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializered_data = self.get_serializer(instance).data
        return Response({
            "status":status.HTTP_200_OK,
            "message": f"{serializered_data["id"]}-idli mototsiklning to'liq malumotlari", 
            "data": serializered_data
        })
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            "status":status.HTTP_200_OK,
            "message": "Mototsiklning barcha ma'lumotlari yangilandi", 
            "data": serializer.data
        })
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data =request.data, partial = True)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({
            "status":status.HTTP_200_OK,
            "message": "Mototsiklning ma'lumotlari qisman yangilandi", 
            "data": serializer.data
        })
    
    def delete(self,request, *args, **kwargs):
        instance = self.get_object()
        serializered_data= self.get_serializer(instance).data
        instance.delete()
        return Response({
            "status":status.HTTP_204_NO_CONTENT,
            "message": f"{serializered_data["id"]}-idli mototsikl o'chirildi",  
            "data": serializered_data
        })