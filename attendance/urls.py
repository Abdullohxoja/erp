from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, AttendanceRecordViewSet

# Create a router and register the viewsets
router = DefaultRouter()
router.register(r'attendances', AttendanceViewSet, basename='attendance')
router.register(r'attendance-records', AttendanceRecordViewSet, basename='attendance-record')

urlpatterns = [
    path('', include(router.urls)),
]
