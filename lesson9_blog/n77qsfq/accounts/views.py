from django.shortcuts import render
from .models import CustomUser
from .serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class SignUpView(GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "response": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(GenericAPIView):
    serializer_class = SignUpSerializer    
    def post(self, request):
        # serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid():
        #     user = serializer.save()
        
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        
        if not user:
            raise ValidationError({"message":"User not found", "status": status.HTTP_400_BAD_REQUEST})
        
        token, created = Token.objects.get_or_create(user=user)
        
        response = {
            'username': user.username,
            'token': token.key,
            'status': status.HTTP_200_OK
        }
        
        return Response(response)
            
            
class LogoutView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            {"message": "Tizimdan muvaffaqiyatli chiqildi."}, 
            status=status.HTTP_200_OK
        )