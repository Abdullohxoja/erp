from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeworkViewSet

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'homework', HomeworkViewSet, basename='homework')

urlpatterns = [
    path('', include(router.urls)),
]
