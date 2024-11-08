from django.contrib import admin

from apps.common import models


@admin.register(models.VersionHistory)
class VersionHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "version", "required", "created_at", "updated_at")
    list_display_links = ("id", "version")
    list_filter = ("required", "created_at", "updated_at")
    search_fields = ("version",)
