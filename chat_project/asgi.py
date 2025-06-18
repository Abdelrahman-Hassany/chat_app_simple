import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat_app.routing

'''
- entry point for the ASGI server
- Routes incoming HTTP and WebSocket connections to the correct handlers

'''

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat_app.routing.websocket_urlpatterns
        )
    ),
})