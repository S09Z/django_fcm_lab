from django.test import TestCase
from django.urls import reverse

class MessagingTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Send FCM Message")
