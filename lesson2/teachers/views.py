from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.exceptions import ValidationError
# Create your views here.


class TeacherListCreateView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many = True)
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Barcha uqituvchilar",
            "data":serializer.data
            })

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save()
        return Response({
            "status": status.HTTP_201_CREATED,
            "message": "Muvaffaqiyatli",
            "data": serializer.data
        })

class TeacherDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
            })
    
    def patch(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(instance = teacher, data = request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
            })
    
    def put(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSerializer(instance = teacher, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
            })
    
    def delete(self, request, pk):
        teacher = get_object_or_404(Teacher, pk=pk)
        teacher.delete()
        return Response({
            "status":status.HTTP_204_NO_CONTENT,
            "message":"Muvaffaqiyatli o'chirildi",
            })
