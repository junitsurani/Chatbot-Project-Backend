from django.shortcuts import render
from rest_framework import viewsets
from .models import ChatbotSettings, ChatbotInteraction
from .serializers import ChatbotSettingsSerializer, ChatbotInteractionSerializer

# Create your views here.

class ChatbotSettingsViewSet(viewsets.ModelViewSet):
    queryset = ChatbotSettings.objects.all()
    serializer_class = ChatbotSettingsSerializer

class ChatbotInteractionViewSet(viewsets.ModelViewSet):
    queryset = ChatbotInteraction.objects.all()
    serializer_class = ChatbotInteractionSerializer
