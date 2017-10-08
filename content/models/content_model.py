from django.db import models

from tinymce.models import HTMLField
from geek_beacon.users.models import User

class ContentItem(models.Model):
    """Table to hold content items"""

    title = models.CharField(max_length=1000)
    body = HTMLField()
    description = HTMLField()
    author = models.ForeignKey(User)
    thumbnail_image = models.ImageField(upload_to='content/thumbs/', blank = True)
    header_image = models.ImageField(upload_to='content/headers/', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('ContentTag')
    category = models.ForeignKey('ContentCategory')
    layout = models.ForeignKey('ContentLayout')
    content_type = models.ForeignKey('ContentType')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'content'
        db_table = 'content_item'


class ContentTag(models.Model):
    """Table to hold the content tags"""

    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'content'
        db_table = 'content_tag'


class ContentCategory(models.Model):
    """Table to hold the content categories"""

    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'content'
        db_table = 'content_category'


class ContentType(models.Model):
    """Table to hold the content types"""
    CONTENT_TYPES = (
        ('page', 'Page'),
        ('post', 'Post'),
    )

    selected = models.CharField(max_length=20, choices=CONTENT_TYPES)

    def __str__(self):
        return self.selected

    class Meta:
        app_label = 'content'
        db_table = 'content_type'


class ContentLayout(models.Model):
    """Table to hold the content layouts"""
    CONTENT_LAYOUTS = (
        ('full', 'Full Width (No Sidebar)'),
        ('sidebar', 'Sidebar'),
    )

    selected = models.CharField(max_length=20, choices=CONTENT_LAYOUTS)

    def __str__(self):
        return self.selected

    class Meta:
        app_label = 'content'
        db_table = 'content_layout'



class PublishHistory(models.Model):
    """Table to hold the history of published content
    (Use this to find live content)
    """

    content_item = models.ForeignKey(ContentItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField()

    def __str__(self):
        return self.content_item.title

    class Meta:
        app_label = 'content'
        db_table = 'content_publish_history'


class FeatureHistory(models.Model):
    """Table to hold the history of featured content
    (Use this to find featured content)
    """

    content_item = models.ForeignKey(ContentItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField()
    image = models.ImageField(upload_to='content/featured/', blank = True)

    def __str__(self):
        return self.content_item.title

    class Meta:
        app_label = 'content'
        db_table = 'content_feature_history'
