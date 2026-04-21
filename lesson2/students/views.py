from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404



class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Barcha uquvchilar",
            "data":serializer.data
        })
    

class StudentCreateView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status":status.HTTP_201_CREATED,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
        })
        raise ValidationError(status.HTTP_400_BAD_REQUEST)


class StudentDetailView(APIView):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk =pk)
        serializer = StudentSerializer(student)
        return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
        })
    

class StudentPartialUpdateView(APIView):
    def patch(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(data = request.data, instance=student, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
        })
    

class StudentUpdateView(APIView):
    def put(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        serializer = StudentSerializer(instance=student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status":status.HTTP_200_OK,
            "message":"Muvaffaqiyatli",
            "data":serializer.data
        })
    

class StudentDeleteView(APIView):
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk = pk)
        student.delete()
        return Response({
            "status":status.HTTP_204_NO_CONTENT,
            "message":"Muvaffaqiyatli uchirildi"
        })
    