from .models import Book
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status
from django.utils.html import escape


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


    def validate_title(self, value):
        if value:
            if len(value) < 2:
                raise ValidationError("Sarlavha kamida 2ta harf bo'lsin")
        return escape(value)   
    
    def validate_author(self, value):
        if value:
            if any(char.isdigit() for char in value):
                raise ValidationError("Muallif ismida son bo'lishi mumkin emas")
            
        return escape(value)

    def validate_price(self, value):
        if value is None:
            raise ValidationError("Narxi yuq bo'lishi mumkin emas")
        
        if value < 0:
            raise  ValidationError("Narxi manfi bo'lmasin")
        
        return value
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            "message":"Ruyxat",
            "status": status.HTTP_200_OK
        })
        return data

    def create(self, validated_data):
        validated_data["title"]= validated_data.get("title").lower()
        validated_data["author"] = validated_data.get("author").lower()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title).lower() #uzgartirmasa eskisi qoladi
        instance.author = validated_data.get('author', instance.author).lower()
        instance.price = validated_data.get('price', instance.price)
        
        instance.save()
        return instance