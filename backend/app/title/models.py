import uuid

from django.db import models
from django.utils.text import slugify

from backend.app.author.models import Author
from backend.app.genre.models import Genre
from backend.app.publisher.models import Publisher
from backend.app.tag.models import Tag


class Publisher(models.Model):
    class TypeChoices(models.TextChoices):
        MANGA = "manga", "Manga"
        MANHWA = "manhwa", "Manhwa"
        MANHUA = "manhua", "Manhua"
        OEL_MANGA = "oel-manga", "OEL Manga"

    class StatusChoices(models.TextChoices):
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"
        DISCONTINUED = "discontinued", "Discontinued"
        ANNOUNCED = "announced", "Announced"

    class ReleaseChoices(models.TextChoices):
        YONKOMA = "yonkoma", "Yonkoma"
        ANTHOLOGY = "anthology", "Anthology"
        DOUJINSHI = "doujinshi", "Doujinshi"
        COLORED = "colored", "Colored"
        ONE_SHOT = "one-shot", "One Shot"
        WEB = "web", "Web"
        WEBTOON = "webtoon", "Webtoon"

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True, blank=True)
    alternative_title = models.CharField(max_length=255, unique=True, null=True)
    description = models.TextField()
    cover = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20, choices=TypeChoices, default=TypeChoices.MANGA
    )
    status = models.CharField(
        max_length=20, choices=StatusChoices, default=StatusChoices.ONGOING
    )
    release_format = models.CharField(max_length=20, choices=ReleaseChoices, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="titles")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="titles"
    )
    tags = models.ManyToManyField(Tag, related_name="titles")
    genres = models.ManyToManyField(Genre, related_name="titles")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
