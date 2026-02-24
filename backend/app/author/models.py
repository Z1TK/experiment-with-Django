import uuid

from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, blank=True)
    pseudunym = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField(null=True)
    image = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
