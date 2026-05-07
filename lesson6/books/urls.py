from .views import *
from django.urls import path


urlpatterns = [
    path("", BookListAPIView.as_view(), name="list"),
    path("create/", BookCreateAPIView.as_view(), name="create"),
    path("update/<int:pk>/", BookUpdateAPIView.as_view(), name="update"),
    path("detail/<int:pk>/", BookRetrieveAPIView.as_view(), name="detail"),
    path("delete/<int:pk>", BookDestroyAPIView.as_view(), name="delete"),
]