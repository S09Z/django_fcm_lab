# fcm_app/admin.py
from django.contrib import admin
from .models import FCMToken

admin.site.register(FCMToken)
