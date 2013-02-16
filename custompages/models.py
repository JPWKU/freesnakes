from django.db import models
from mezzanine.pages.models import Page


class CustomPage(Page):
    short_name = models.CharField(max_length=255)
    long_name = models.CharField(max_length=512)
