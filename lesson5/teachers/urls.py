from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path("generic/", TeacherGenericView.as_view(), name="teacher-generic"),
    path("generic/<int:pk>/", TeacherGenericView.as_view(), name="teacher-generic"),
    path('', include(router.urls)),
]
