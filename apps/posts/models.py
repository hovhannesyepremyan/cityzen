from django.db import models

from apps.core.helpers import get_file_path


class Post(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to=get_file_path)
    description = models.TextField()
    district = models.ForeignKey("core.District", on_delete=models.CASCADE, null=True, blank=True)
    # TODO: remove null and blank during removing db
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
