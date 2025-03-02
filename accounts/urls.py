from django.urls import path
from accounts import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
]
