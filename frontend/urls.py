
from django.urls import path, include
from .views import index, info
urlpatterns = [
    path('', index),
    path('ToolInfo/', info)
]