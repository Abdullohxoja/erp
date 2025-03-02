from rest_framework import serializers
from .models import Attendance, AttendanceRecord
from accounts.models import User
from groups.models import Group

# Serializer for Attendance
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'group', 'date', 'created_by']  # Include necessary fields

# Serializer for AttendanceRecord
class AttendanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceRecord
        fields = ['id', 'attendance', 'student', 'is_present']  # Include necessary fields
