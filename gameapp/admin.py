from django.contrib import admin
from .models import *

# Register your models here.
class GamePostAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'description', 'like_count', 'dislike_count',)

class ReplyAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'description', 'reply',)

admin.site.register(GamePost,GamePostAdmin)
admin.site.register(Reply,ReplyAdmin)
