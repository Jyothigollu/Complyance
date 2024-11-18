from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    country = models.CharField(max_length=100, blank=True, null=True)  # Selected country
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Viewer', 'Viewer')], default='Viewer')

    def __str__(self):
        return self.username

# DataModel definition (Added)
class DataModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Reference to CustomUser model
    data_field = models.CharField(max_length=255)  # Field to store some data
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record is created

    def __str__(self):
        return f"{self.user.username} - {self.data_field}"




