from django.contrib import admin
from .models import ChatMessage  # Import the ChatMessage model from your models.py

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'content')
