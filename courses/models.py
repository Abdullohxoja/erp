from django.db import models
from accounts.models import User
from groups.models import Group

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='lessons/')


    def __str__(self):
        return self.title