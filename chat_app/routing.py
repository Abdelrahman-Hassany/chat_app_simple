from django.urls import re_path
from . import consumers

'''
- WebSocket routing configuration
- Maps WebSocket URL paths to their corresponding consumers 

'''
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]