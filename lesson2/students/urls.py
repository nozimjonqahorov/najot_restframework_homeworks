from django.urls import path
from .views import * 

urlpatterns = [
    path("", StudentListView.as_view(), name="list"),
    path("create/", StudentCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", StudentDetailView.as_view(), name="detail"),
    path("update-partial/<int:pk>/", StudentPartialUpdateView.as_view(), name="partial-update"),
    path("update/<int:pk>/", StudentUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", StudentDeleteView.as_view(), name="delete"),
]
