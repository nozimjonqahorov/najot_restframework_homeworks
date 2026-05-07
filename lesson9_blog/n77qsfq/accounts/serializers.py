from .models import CustomUser
from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate


class SignUpSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    
    def validate(self, attrs):
        password = attrs.get('password', None)
        password_confirm = attrs.get('password_confirm', None)
        
        if password and password_confirm and password != password_confirm:
            raise ValidationError('Parollar mos emas')
        
        if len(password) < 5:
            raise ValidationError('Parol uzunligi 5 tadan kop bolsin')
        
        return super().validate(attrs)
    
    def validate_email(self, value):
        x = value.split('@') #HOJIAKBAR01@gamil.com ['HOJIAKBAR01', 'gamil.com']
        if '@' not in value or len(x[0])<5 or int(len(x[1])) < 3 or '.' not in x[1][1:len(x[1])-1]:
            raise ValidationError('Xato email') 
        return value
        
        
    def create(self, validated_data):
        validated_data.pop('password_confirm')  # 👈 BU SHART

        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(
            **validated_data,
            password=password
        )

        return user
    
    
    def to_representation(self, instance):
        user =  super().to_representation(instance)
        return {
            "username": user.get("username", ''),
            "first_name": user["first_name"],
            "message": "User created"
        }
    
    

        
        

