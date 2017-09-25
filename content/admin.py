from django.contrib import admin
from .models import * 

admin.site.register(ContentItem)
admin.site.register(ContentTag)
admin.site.register(ContentType)
admin.site.register(ContentCategory)
admin.site.register(ContentLayout)
admin.site.register(MenuItem)
admin.site.register(PublishHistory)
admin.site.register(FeatureHistory)
