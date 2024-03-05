from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/some_path/", YourConsumer.as_asgi()),
    ]),
})
