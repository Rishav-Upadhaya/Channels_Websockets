from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/somepath/", consumers.YourConsumer.as_asgi()),
]