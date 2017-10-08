from django.db import models



class MenuItem(models.Model):
    """Table to hold menu items"""

    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    content = models.ForeignKey('ContentItem', blank=True, null=True)
    override_url = models.CharField(max_length=1000, blank=True, null=True)
    priority = models.IntegerField()
    published = models.BooleanField()

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'content'
        db_table = 'content_menu_item'
