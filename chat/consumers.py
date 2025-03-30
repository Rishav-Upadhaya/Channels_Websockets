from channels.generic.websocket import WebsocketConsumer
import json

class YourConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            "type" : "Connection Established!",
            "message": "Connected!"
            }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        pass