
# groups/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'groups', views.GroupViewSet, basename='groups')  # Add basename

urlpatterns = [
    path('', include(router.urls)),
]