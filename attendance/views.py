from rest_framework import viewsets
from .models import Attendance, AttendanceRecord
from .serializers import AttendanceSerializer, AttendanceRecordSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Attendance
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]  # Optional: Ensure the user is authenticated

# ViewSet for AttendanceRecord
class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]  # Optional: Ensure the user is authenticated
