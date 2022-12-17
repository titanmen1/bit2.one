from django.contrib import admin
from shortener.models import Urls


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'full_url', 'created_at', 'updated_at')
