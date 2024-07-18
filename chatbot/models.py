from django.db import models

# Create your models here.

class ChatbotSettings(models.Model):
    main_color = models.CharField(max_length=7, default="#6fd6ed")
    send_message_color = models.CharField(max_length=7, default="#6fd6ed")
    received_message_color = models.CharField(max_length=7, default="#ffffff")
    background_color = models.CharField(max_length=7, default="#ffffff")
    send_message_text_color = models.CharField(max_length=7, default="#ffffff")
    received_message_text_color = models.CharField(max_length=7, default="#4b5563")

class ChatbotInteraction(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
