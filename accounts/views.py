from django.shortcuts import render
from .models import User

def user_list(request):
    # Optionally, you can filter users by role
    role_filter = request.GET.get('role', None)  # Get role from URL query params
    if role_filter and role_filter in dict(User.ROLES):
        users = User.objects.filter(role=role_filter)
    else:
        users = User.objects.all()

    return render(request, 'user_list.html', {'users': users})
