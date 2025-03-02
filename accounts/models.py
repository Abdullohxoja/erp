from django.db import models
from django.contrib.auth.models import AbstractUser


# Base User Model
class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='student')

    # Remove the default groups and permissions fields
    groups = None
    user_permissions = None


# Admin Profile Model
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Admin)"


# Teacher Profile Model
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    subjects = models.ManyToManyField('Course', related_name='subject_teachers')  # Changed related_name

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} (Teacher)"


# Student Profile Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=20, unique=True)
    course = models.ManyToManyField('Course', related_name='enrolled_students')  # Changed related_name

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.student_id})"


# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    teachers = models.ManyToManyField(Teacher, related_name='courses_taught')  # Changed related_name
    students = models.ManyToManyField(Student, related_name='courses_enrolled')  # Changed related_name

    def __str__(self):
        return f"{self.code} - {self.name}"
