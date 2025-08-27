"""
ASGI config for inventory_tracker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import inventory_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventory_tracker.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            inventory_app.routing.websocket_urlpatterns
        )
    ),
})
