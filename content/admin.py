from django.contrib import admin
from content.models.content_model import *
from content.models.menu_model import MenuItem

admin.site.register(ContentItem)
admin.site.register(ContentTag)
admin.site.register(ContentType)
admin.site.register(ContentCategory)
admin.site.register(ContentLayout)
admin.site.register(MenuItem)
admin.site.register(PublishHistory)
admin.site.register(FeatureHistory)
