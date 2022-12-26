from django.db import models
from shortener.utils import create_shortened_url


class Shortener(models.Model):
    short_url = models.URLField(null=True)
    full_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_url
