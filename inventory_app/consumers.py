from channels.generic.websocket import AsyncWebsocketConsumer
import json

class InventoryConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("inventory", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("inventory", self.channel_name)

    # Custom message from views.py
    async def send_notification(self, event):
        message = event['message']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
