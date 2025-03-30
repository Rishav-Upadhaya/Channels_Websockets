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
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print('Message: ', message )

        self.send(text_data=json.dumps({
            'type' : 'chat',
            'message' : message
        }))