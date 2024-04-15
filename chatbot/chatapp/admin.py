from django.contrib import admin
from .models import ChatRoom,ChatMessage
# Register your models here.

admin.site.register(ChatRoom)
# @admin.register(ChatRoom)
# class ChatRoomAdmin(admin.ModelAdmin):
#     fields = ['name','slug']

admin.site.register(ChatMessage)
    
    
    



