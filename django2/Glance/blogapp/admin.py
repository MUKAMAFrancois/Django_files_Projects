from django.contrib import admin
from.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','updated']
    list_filter=('title','created')
    search_fields=('title','author')
    ordering=('publish','created')
    prepopulated_fields={'slug':('title',)}
