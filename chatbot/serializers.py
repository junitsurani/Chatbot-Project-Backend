from rest_framework import serializers
from .models import ChatbotSettings, ChatInteraction

class ChatbotSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatbotSettings
        fields = '__all__'

class ChatInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatInteraction
        fields = ['user_message', 'bot_response', 'timestamp']
