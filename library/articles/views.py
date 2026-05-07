from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from .models import Article
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def article_create(request):
    serializer = ArticleSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})
    
@api_view(["PUT"])
def article_update(request, pk):
    article = Article.objects.filter(pk=pk).first()
    serializer = ArticleSerializer(data = request.data, instance = article)
    if serializer.is_valid():
        serializer.save()
        return Response({
                "status":status.HTTP_200_OK,
                "message": "Yangilandi",
                "data": serializer.data         
            })
    raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})

@api_view(["PATCH"])
def article_partial_update(request, pk):
    article = Article.objects.filter(pk=pk).first()
    serializer = ArticleSerializer(data = request.data, instance = article, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
                "status":status.HTTP_200_OK,
                "message": "Yangilandi",
                "data": serializer.data         
            })
    raise ValidationError({"status":status.HTTP_400_BAD_REQUEST, "message":"Xato ma'lumot yuborildi"})

@api_view(["DELETE"])
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)  
    article.delete()
    return Response({"message": "O'chirildi"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    serializer = ArticleSerializer(article)
    return Response({
        "status": status.HTTP_200_OK,
        "data": serializer.data
    }, status=status.HTTP_200_OK)