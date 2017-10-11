from __future__ import absolute_import, unicode_literals

from datetime import datetime

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from wagtail.wagtailsearch import index


class HomePage(Page):
    pass


class SinglePage(Page):
    date = models.DateTimeField("Post date", default=datetime.now)
    subtitle = models.CharField(max_length=250, blank=True)
    header_image = models.ForeignKey('wagtailimages.Image',
                                     on_delete=models.SET_NULL, related_name='+', blank=True, null=True,)

    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('subtitle'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('header_image'),
    ]
