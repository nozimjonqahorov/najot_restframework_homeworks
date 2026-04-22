from django.urls import path
from .views import *

urlpatterns = [
    path("", notebook_list, name="list"),
    path("create/", notebook_create, name="create"),
    path("detail/<int:pk>/", notebook_detail, name="detail"),
    path("update/<int:pk>/", notebook_update, name="update"),
    path("partial-update/<int:pk>/", notebook_partial_update, name="partial-update"),
    path("delete/<int:pk>/", notebook_delete, name="delete"),
    path("list-create/", notebook_list_create_view, name="list-create"),
    path("detail-update-delete/<int:pk>/", notebook_detail_update_delete_view, name="detail-update-delete"),
]
