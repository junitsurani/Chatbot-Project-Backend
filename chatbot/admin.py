from django.contrib import admin
from .models import ChatbotSettings, ChatInteraction

class ChatBotSettingsService(admin.ModelAdmin):
    list_display = ('main_color', 'send_message_color', 'received_message_color', 'background_color', 'send_message_text_color', 'received_message_text_color', 'launcher_icon', 'assistant_image', 'assistant_avatar', 'send_icon')

class ChatInteractionAdmin(admin.ModelAdmin):
    list_display = ('user_message', 'bot_response', 'timestamp')

admin.site.register(ChatbotSettings, ChatBotSettingsService)
admin.site.register(ChatInteraction, ChatInteractionAdmin)
