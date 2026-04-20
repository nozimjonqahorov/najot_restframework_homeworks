from django.urls import path
from .views import *

urlpatterns = [
    path("list-create/", phone_list_create, name="list-create"),
    path("detail-update-delete/<int:pk>/", phone_detail_update_delete, name="detail=update-delete")
    
]
