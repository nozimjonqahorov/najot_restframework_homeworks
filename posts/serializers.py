from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "author", "title", "content", "is_premium", "created_at", "updated_at"]
    


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "is_premium"]