from django.contrib import admin
from .models import Document, ChatMessage, AIResponse

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'upload_date')
    list_filter = ('user', 'upload_date')
    search_fields = ('title', 'user__username')
    
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'content')

@admin.register(AIResponse)
class AIResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'content')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username', 'content')
