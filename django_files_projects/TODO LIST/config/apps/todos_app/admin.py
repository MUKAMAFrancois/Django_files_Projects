from django.contrib import admin
from apps.todos_app.models import TodoModel

# Register your models here.
@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display=('title','category','due_date')
    list_filter=('category',)
    ordering=('due_date',)
    search_fields=('category','title','description')