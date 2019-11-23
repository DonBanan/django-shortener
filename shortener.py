import random

from django.conf import settings

from .models import ShortUrl


def get_short_url(length):
    dictionary = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz234567890"
    return ''.join(random.choice(dictionary) for _ in range(length))


def create(post_one):
    length_url = settings.SHORTEN_LENGTH_URL
    if ShortUrl.objects.filter(original_url__exact=post_one.get_absolute_url()).exists():
        return ShortUrl.objects.get(original_url=post_one.get_absolute_url())
    ShortUrl.objects.create(original_url=post_one.get_absolute_url(),
                            short_url=get_short_url(length_url),
                            content_object=post_one)
