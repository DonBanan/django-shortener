from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View

from .models import ShortUrl


class RedirectView(View):

    def get(self, request, short):
        url = get_object_or_404(ShortUrl, short_url=short)
        return redirect(url.original_url)
