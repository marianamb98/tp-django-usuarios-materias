from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=30, blank=True)
    direccion = models.CharField(max_length=120, blank=True)
    localidad = models.CharField(max_length=80, blank=True)
    codigo_postal = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username