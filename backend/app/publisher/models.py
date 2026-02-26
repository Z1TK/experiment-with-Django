import uuid

from django.db import models
from django.utils.text import slugify


class Publisher(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    another_name = models.CharField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='backend/images/publishers/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
