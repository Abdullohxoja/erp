from rest_framework import serializers
from .models import Group
from accounts.models import User


class GroupSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(role='student'),
        required=False
    )
    teachers = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(role='teacher'),
        required=False
    )
    created_by = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'description',
            'students',
            'teachers',
            'created_by'
        ]
        read_only_fields = ['created_by']

    def validate(self, data):
        """
        Custom validation:
        - Ensure admin isn't assigning themselves as student/teacher
        - Prevent empty group creation
        """
        request = self.context.get('request')

        # Check for self-assignment
        if request:
            current_user = request.user
            students = data.get('students', [])
            teachers = data.get('teachers', [])

            if current_user in students:
                raise serializers.ValidationError("Admins cannot be students in their own groups")

            if current_user in teachers:
                raise serializers.ValidationError("Admins cannot be teachers in their own groups")

        # Check for empty group
        if not data.get('students') and not data.get('teachers'):
            raise serializers.ValidationError("Group must have at least one student or teacher")

        return data

    def create(self, validated_data):
        """
        Custom create method to handle M2M relationships
        """
        students = validated_data.pop('students', [])
        teachers = validated_data.pop('teachers', [])

        group = Group.objects.create(**validated_data)

        # Add relationships after creation
        group.students.set(students)
        group.teachers.set(teachers)

        return group

    def update(self, instance, validated_data):
        """
        Custom update method to handle M2M relationships
        """
        students = validated_data.pop('students', None)
        teachers = validated_data.pop('teachers', None)

        instance = super().update(instance, validated_data)

        if students is not None:
            instance.students.set(students)
        if teachers is not None:
            instance.teachers.set(teachers)

        return instance