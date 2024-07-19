from django.db import models

class ChatbotSettings(models.Model):
    main_color = models.CharField(max_length=7, default="#6fd6ed")
    send_message_color = models.CharField(max_length=7, default="#6fd6ed")
    received_message_color = models.CharField(max_length=7, default="#ffffff")
    background_color = models.CharField(max_length=7, default="#ffffff")
    send_message_text_color = models.CharField(max_length=7, default="#ffffff")
    received_message_text_color = models.CharField(max_length=7, default="#4b5563")

    # Image fields
    launcher_icon = models.ImageField(upload_to='chatbot_images/', blank=True, null=True)
    assistant_image = models.ImageField(upload_to='chatbot_images/', blank=True, null=True)
    assistant_avatar = models.ImageField(upload_to='chatbot_images/', blank=True, null=True)
    send_icon = models.ImageField(upload_to='chatbot_images/', blank=True, null=True)

    def __str__(self):
        return f"Chatbot Settings: {self.pk}"

class ChatInteraction(models.Model):
    user_message = models.TextField(blank=True, null=True)
    bot_response = models.TextField(blank=True, null=True)  
    timestamp = models.DateTimeField(auto_now_add=True)
