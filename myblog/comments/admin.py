from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display=['ip','city','created_time']
    list_filter=['created_time']

admin.site.register(Comment,CommentAdmin)
