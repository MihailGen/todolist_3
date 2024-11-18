from django.contrib import admin
from .models import Task, Comment, Tag


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'due_date')
    search_fields = ('name', 'description')
    list_filter = ('due_date', 'author')


    inlines = [
        CommentInline,
    ]

admin.site.register(Tag)