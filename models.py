from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ShortUrl(models.Model):
    original_url = models.CharField('Original URL', max_length=2000, unique=True, db_index=True)
    short_url = models.CharField('Short url', max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return '{} - {}'.format(self.short_url, self.original_url)
