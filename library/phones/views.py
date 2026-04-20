from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PhoneSerializer
from rest_framework.decorators import api_view
from .models import Phone
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def phone_list_create(request):
    if request.method == "GET":
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = PhoneSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def phone_detail_update_delete(request, pk):
    if request.method == "GET":
        phone = get_object_or_404(Phone, pk=pk)
        serializer = PhoneSerializer(phone)
        return Response({
            "status": status.HTTP_200_OK,
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    if request.method == "PUT":
        phone = Phone.objects.filter(pk=pk).first()
        serializer = PhoneSerializer(data = request.data, instance = phone)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    "status":status.HTTP_200_OK,
                    "message": "Yangilandi",
                    "data": serializer.data         
                })
        raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})
    
    if request.method == "PATCH":
        phone = Phone.objects.filter(pk=pk).first()
        serializer = PhoneSerializer(data = request.data, instance = phone, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    "status":status.HTTP_200_OK,
                    "message": "Yangilandi",
                    "data": serializer.data         
                })
        raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})
    
    if request.method == "DELETE":
        phone = get_object_or_404(Phone, pk=pk)  
        phone.delete()
        return Response({"message": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)
    
    
        

