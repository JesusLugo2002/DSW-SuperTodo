from django.contrib import admin

from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "deadline", "done", "created_at", "updated_at"]
    list_filter = ["done"]