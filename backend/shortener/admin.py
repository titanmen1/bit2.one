from django.contrib import admin
from shortener.models import Shortener


@admin.register(Shortener)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'full_url', 'created_at', 'updated_at')
