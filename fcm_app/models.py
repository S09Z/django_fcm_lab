# fcm_app/models.py
from django.db import models
from django.contrib.auth.models import User

class FCMToken(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)
