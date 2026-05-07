from django.urls import path
from .views import article_list, article_create, article_update, article_partial_update, article_detail, article_delete
urlpatterns = [
    path("", article_list, name="list"),
    path("create/", article_create, name="create"),
    path("update/<int:pk>/", article_update, name="update"),
    path("partial-update/<int:pk>/", article_partial_update, name="partial_update"),
    path("detail/<int:pk>/", article_detail, name="detail"),
    path("delete/<int:pk>/", article_delete, name="delete"),

]
