from django.db import models


class Urls(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    short_url = models.URLField(null=True)
    full_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    # count = models.IntegerField(default=0)

    def __str__(self):
        return self.full_url
