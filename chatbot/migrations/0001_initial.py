# Generated by Django 4.2.6 on 2024-07-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatbotInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField()),
                ('bot_response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatbotSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_color', models.CharField(default='#6fd6ed', max_length=7)),
                ('send_message_color', models.CharField(default='#6fd6ed', max_length=7)),
                ('received_message_color', models.CharField(default='#ffffff', max_length=7)),
                ('background_color', models.CharField(default='#ffffff', max_length=7)),
                ('send_message_text_color', models.CharField(default='#ffffff', max_length=7)),
                ('received_message_text_color', models.CharField(default='#4b5563', max_length=7)),
            ],
        ),
    ]
