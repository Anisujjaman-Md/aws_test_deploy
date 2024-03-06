
from django.urls import re_path
from notifaction_test.consumer import NotificationConsumer



websocket_urlpatterns = [
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
]
