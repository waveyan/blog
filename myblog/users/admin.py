from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','nickname']
    search_fields=['username','email','nickname']

admin.site.register(User,UserAdmin)
