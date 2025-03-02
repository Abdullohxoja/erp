from rest_framework import viewsets
from .models import Homework
from .serializers import HomeworkSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Homework
class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]  # Optional: Ensure the user is authenticated
