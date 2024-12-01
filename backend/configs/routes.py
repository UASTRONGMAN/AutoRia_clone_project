from django.urls import path

from channels.routing import URLRouter

from apps.chat.routes import websocket_urlpatterns as chat_routes

websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routes)),
]