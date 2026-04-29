from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status, viewsets



class TeacherGenericView(GenericAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_object(self, pk):
        return get_object_or_404(Teacher, pk=pk)

    def get(self, request, pk=None):
        if pk:
            teacher = self.get_object(pk) 
            serializer = self.get_serializer(teacher)
            return Response({
                "status": status.HTTP_200_OK,
                "data": serializer.data
            })
        
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "status": status.HTTP_200_OK,
            "soni": queryset.count(),
            "data": serializer.data
        })

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response({
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Obyekt o'chirildi"
        })

    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = self.get_serializer(instance=teacher, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": status.HTTP_200_OK,
            "data": serializer.data 
        })

    def patch(self, request, pk):
        teacher = self.get_object(pk)
        serializer = self.get_serializer(instance=teacher, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "status": status.HTTP_200_OK,
            "data": serializer.data
        })  
    


####################################################################################################################
####################################################################################################################


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



#############################################################################################################


class LessonViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Lesson.objects.all()
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Lesson.objects.all()
        lesson = get_object_or_404(queryset, pk=pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    def update(self, request, pk=None):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        lesson = get_object_or_404(Lesson, pk=pk)
        serializer = LessonSerializer(lesson, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        lesson = get_object_or_404(Lesson, pk=pk)
        lesson.delete()
        return Response({"message": "Dars o'chirildi"}, status=status.HTTP_204_NO_CONTENT)