from django.urls import path
from .views import *
urlpatterns = [
    path("list-create/",TeacherListCreateView.as_view(), name="teacher-list-create"),
    path("detail-update-delete/<int:pk>", TeacherDetailUpdateDeleteView.as_view(), name="detail-update-delete"),
]
