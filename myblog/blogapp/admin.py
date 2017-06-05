from django.contrib import admin
from .models import Post,Category,Tag,Url,Sentence

class PostInline(admin.StackedInline):
    '''在category里编辑1篇文章'''
    model=Post
    extra=1

class CategoryAdmin(admin.ModelAdmin):
    inlines=[PostInline]
    list_display=['id','name']
    list_filter=['id']

class PostAdmin(admin.ModelAdmin):
    search_fields=['title','author']
    list_display=['title','excerpt','created_time','modified_time']
    list_filter=['created_time','modified_time']

class TagAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_filter=['id']

class UrlAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','url','created_time']
    list_filter=['created_time']

class SentenceAdmin(admin.ModelAdmin):
    search_field=['sentence','originate_from']
    list_display=['sentence','originate_from','created_time']
    list_filter=['created_time','originate_from']


admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Url,UrlAdmin)
admin.site.register(Sentence,SentenceAdmin)
