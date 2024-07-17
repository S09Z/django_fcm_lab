# fcm_app/management/commands/send_test_message.py
from django.core.management.base import BaseCommand
from firebase_admin import messaging

class Command(BaseCommand):
    help = 'Send a test message to FCM'

    def handle(self, *args, **kwargs):
        # Replace 'your-device-token' with a valid FCM registration token
        valid_token = 'BOrNGXnv77alDrPVeu3Beo5_CxaVOU4zKjbEA7HtbJhBJWwHGMWa0m8P9wo4o9osTJSYQ3X4LElEKTGTbEDeRJw'

        message = messaging.Message(
            notification=messaging.Notification(
                title='Test Message',
                body='This is a test message from FCM.',
            ),
            token=valid_token,
        )

        response = messaging.send(message)
        print(f'Successfully sent message: {response}')
