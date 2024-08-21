from django.db import models

from core.helpers import get_file_path


class District(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True, blank=True, upload_to=get_file_path)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name