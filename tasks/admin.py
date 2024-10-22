from django.contrib import admin

from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "complete_before", "done", "created_at", "updated_at"]
    list_filter = ["done"]