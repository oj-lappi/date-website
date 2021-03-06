import logging

from ckeditor.fields import RichTextField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger('date')

POST_SLUG_MAX_LENGTH = 50

class StaticPageNav(models.Model):
    category_name = models.CharField(_('Kategori'), max_length=255, blank=False)

    def __str__(self):
        return self.category_name

class StaticPage(models.Model):
    title = models.CharField(_('Titel'), max_length=255, blank=False)
    content = RichTextField(_('Innehåll'), blank=True)
    created_time = models.DateTimeField(_('Skapad'), default=timezone.now)
    modified_time = models.DateTimeField(_('Modifierad'), editable=False, null=True, blank=True)
    slug = models.SlugField(_('Slug'), unique=True, allow_unicode=False, max_length=POST_SLUG_MAX_LENGTH)
    category = models.ForeignKey(StaticPageNav, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def update(self):
        self.modified_time = timezone.now()
        self.save()