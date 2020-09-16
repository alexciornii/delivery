from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from apps.market.consumer import MarketConsumer
from django.urls import re_path


application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'market$', MarketConsumer)
        ])
    ),
})
