# Generated by Django 4.2.6 on 2024-07-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_rename_message_chatinteraction_bot_response_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotsettings',
            name='assistant_avatar',
            field=models.ImageField(blank=True, null=True, upload_to='chatbot_images/'),
        ),
        migrations.AddField(
            model_name='chatbotsettings',
            name='assistant_image',
            field=models.ImageField(blank=True, null=True, upload_to='chatbot_images/'),
        ),
        migrations.AddField(
            model_name='chatbotsettings',
            name='launcher_icon',
            field=models.ImageField(blank=True, null=True, upload_to='chatbot_images/'),
        ),
        migrations.AddField(
            model_name='chatbotsettings',
            name='send_icon',
            field=models.ImageField(blank=True, null=True, upload_to='chatbot_images/'),
        ),
    ]
