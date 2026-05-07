from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer, PostCreateSerializer
from .models import Post
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import ISAuthorOrReadOnly, IsAdminOrReadOnly, IsOwnerOrAdmin





class PostListApiView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    
# class PostListApiView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostCreateApiView(APIView):

    permission_classes = [IsAuthenticated, ]
    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(author = request.user)
            
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "Post yaratildi",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Xatolik yuz berdi",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    


class PostDetailApiView(APIView):
    permission_classes = [IsOwnerOrAdmin]
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, obj=post)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateApiView(APIView):
    permission_classes = [IsAuthenticated, ISAuthorOrReadOnly]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post) 
        return Response(serializer.data)
    

    def put(self, request, pk):
        post = get_object_or_404(Post, pk = pk)

        self.check_object_permissions(request, post)

        serializer = PostCreateSerializer(data = request.data, instance = post)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": status.HTTP_202_ACCEPTED,
                "message": "Post yangilandi",
                "data": serializer.data
            }, status=status.HTTP_202_ACCEPTED)
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Xatolik yuz berdi",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        post = get_object_or_404(Post, pk = pk)

        self.check_object_permissions(request, post)
        serializer = PostCreateSerializer(data = request.data, instance = post, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({
                "status": status.HTTP_202_ACCEPTED,
                "message": "Post yangilandi",
                "data": serializer.data
            },  status=status.HTTP_202_ACCEPTED)
        
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Xatolik yuz berdi",
            "errors": serializer.errors
        },  status=status.HTTP_400_BAD_REQUEST)



class PostDeleteApiView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post) 
        return Response(serializer.data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        self.check_object_permissions(request, post) # Obyekt darajasidagi ruxsatni tekshiradi
        post.delete()
        return Response({
            "status": status.HTTP_204_NO_CONTENT,
            "message": "Post muvaffaqiyatli o'chirildi"
        }, status=status.HTTP_204_NO_CONTENT)