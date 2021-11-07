"""
ASGI config for FallInAPI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
import FallInChat.routing
from django_private_chat2 import urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FallInAPI.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            FallInChat.routing.websocket_urlpatterns
        )
    ),
})