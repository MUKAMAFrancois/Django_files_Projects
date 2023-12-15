from django.contrib import admin
from .models import Post,CommentModel

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['title','author','category','publish','get_tags']
    list_filter=('category','author','publish','created')
    prepopulated_fields={'slug':('title',)}
    search_fields=('author','body')
    date_hierarchy='publish'
    raw_id_fields=('author',)
    ordering=('publish',)

    def get_tags(self, obj):
        return ",".join(o for o in obj.tags.names())

@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display=['name','apost','email','company']
    list_filter=('apost','company','active')
    search_fields=('apost','name','content')
    ordering=('active','created')
