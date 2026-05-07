from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from rest_framework import generics



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostListCreateAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    @extend_schema(request=PostSerializer, responses=PostSerializer)
    def get(self, request):
        print(f"User: {request.user}")
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    @extend_schema(request=PostSerializer, responses=PostSerializer)
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PostDetailUpdateDeleteAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    @extend_schema(request=PostSerializer, responses=PostSerializer)
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    @extend_schema(request=PostSerializer, responses=PostSerializer)
    def put(self, request, pk):
        post = self.get_object(pk)
        
        if post.author != request.user:
            return Response({"error": "Sizda bu postni tahrirlash huquqi yo'q"}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = PostSerializer(post, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=PostSerializer, responses=PostSerializer)
    def delete(self, request, pk):
        post = self.get_object(pk)
        
        if post.author != request.user:
            return Response({"error": "Sizda bu postni o'chirish huquqi yo'q"}, status=status.HTTP_403_FORBIDDEN)
            
        post.delete()
        return Response({"message": "Post o'chirildi"}, status=status.HTTP_204_NO_CONTENT)