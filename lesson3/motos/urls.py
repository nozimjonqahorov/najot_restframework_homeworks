from django.urls import path
from .views import *
urlpatterns = [
    path("list-create", MotoListCreateView.as_view(), name="list-create"),
    path("detail-update-delete/<int:pk>/", MotoDetailUpdateDeleteView.as_view(), name = "detail-update-delete"),
]
