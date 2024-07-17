# fcm_app/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import FCMToken

class FCMTokenModelTest(TestCase):
    def test_str_method(self):
        user = User.objects.create(username='testuser')
        token = FCMToken.objects.create(token='testtoken123', user=user)
        self.assertEqual(str(token), 'testtoken123')
