"""
ASGI config for core project.

"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chats.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)

    "websocket": URLRouter(
        chats.routing.websocket_urlpatterns
    ),
    
})