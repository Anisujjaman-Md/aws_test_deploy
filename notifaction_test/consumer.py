import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Notification

logging.basicConfig(level=logging.DEBUG)  # Add this line for console logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('websocket_log.txt')
file_handler.setLevel(logging.DEBUG)  # Adjust the log level as needed
logger.addHandler(file_handler)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        logger.info("WebSocket connection established.")

    async def receive(self, text_data):
        if text_data:
            try:
                data = json.loads(text_data)
                message_text = data.get('message', '')

                if message_text:
                    Notification.objects.create(message=message_text)

                await self.send(text_data=json.dumps({
                    'message': message_text,
                }))
            except json.JSONDecodeError as e:
                logger.error(f"JSON Decode Error: {e}")
                file_handler.flush()  # Flush the file handler

        data = json.loads(text_data)
        message_text = data.get('message', '')

        if message_text:
            Notification.objects.create(message=message_text)
            logger.info(f"Notification created: {message_text}")

        await self.send(text_data=json.dumps({
            'message': message_text,
        }))
        logger.info("Message sent to WebSocket.")
        file_handler.flush()  # Flush the file handler
