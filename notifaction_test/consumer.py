import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Notification

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data['This is a Sample message']

        Notification.objects.create(message=message_text)

        await self.send(text_data=json.dumps({
            'message': message_text,
        }))
