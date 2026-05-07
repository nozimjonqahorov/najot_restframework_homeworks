from django.urls import path
from .views import *
urlpatterns = [
    path("posts/", PostListCreateAPIView.as_view()),
    path("post-crud/<int:pk>/", PostDetailUpdateDeleteAPIView.as_view()),
    path("category-list-create/", CategoryListCreateAPIView.as_view()),
    path("category-crud/<int:pk>/", CategoryDetailAPIView.as_view())
]
