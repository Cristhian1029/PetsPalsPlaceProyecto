# models.py
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass  # Añade campos personalizados si es necesario
