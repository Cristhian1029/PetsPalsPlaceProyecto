# urls.py
from django.urls import path
from .views import register, profile, update_profile, delete_account

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('delete_account/', delete_account, name='delete_account'),
]
