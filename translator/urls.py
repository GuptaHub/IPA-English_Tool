from django.urls import path
from .views import CreateIPATranslator

urlpatterns = [
    path('', CreateIPATranslator.as_view())
]