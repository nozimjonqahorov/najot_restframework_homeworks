from django.urls import path
from .views import *

# urlpatterns = [
    
# ]

urlpatterns = [
    path("", PostListApiView.as_view(), name="list"),
    path("create/", PostCreateApiView.as_view(), name="create"),
    path("detail/<int:pk>/", PostDetailApiView.as_view(), name="detail"),
    path("update/<int:pk>/", PostUpdateApiView.as_view(), name="update"),
    path("delete/<int:pk>/", PostDeleteApiView.as_view(), name="delete"),
]
