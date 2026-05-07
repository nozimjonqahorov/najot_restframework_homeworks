from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Car
from .serializers import CarSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
# Create your views here.


class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)

        data = {
            "status": 200,
            "soni":queryset.count(),
            "message": "Barcha mashinalar ro'yxati",
            "cars": serializer.data 
        }
        return Response(data)
    

class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED,
            "message": "Yangi mashina muvaffaqiyatli qo'shildi!",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            "status": 200,
            "message": "Mahinaning toliq ma'lumotlari",
            "data": serializer.data 
        }
        return Response(data)



class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response({
            "status": 200,
            "message": "Mashina ma'lumotlari to'liq yangilandi",
            "data": serializer.data
        })
    
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial = True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
    
        return Response({
            "status": 200,
            "message": "Mashina ma'lumotlari qisman yangilandi",
            "data": serializer.data
        })
    

class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer_data = self.get_serializer(instance).data
        instance.delete()
        return Response({
            "status": 204,
            "message": "Quyidagi ID-li mashina o'chirildi",
            "deleted_id": serializer_data["id"]
        })