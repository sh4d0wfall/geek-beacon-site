from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from content.models.menu_model import MenuItem
from content.models.content_model import ContentCategory, ContentTag, ContentLayout, ContentType, ContentItem

from geek_beacon.users.models import User

class AddContentForm(forms.Form):
    """Form to add new content (Post/Page)"""

    title = forms.CharField(label='Title', max_length=100)
    header_image = forms.ImageField(required=False)
    thumbnail_image = forms.ImageField(required=False)
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 90, 'rows': 1}),required=False)
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 90, 'rows': 20}),required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    category = forms.ModelChoiceField(queryset=ContentCategory.objects.all(),required=False)
    tags = forms.ModelMultipleChoiceField(queryset=ContentTag.objects.all(),required=False)
    layout = forms.ModelChoiceField(queryset=ContentLayout.objects.all())
    content_type = forms.ModelChoiceField(queryset=ContentType.objects.all())
    published = forms.BooleanField(required=False)
    featured = forms.BooleanField(required=False)
    featured_image = forms.ImageField(required=False)

    class Meta:
        model = FlatPage


class AddMenuItemForm(forms.Form):
    """Form to add items to the menu"""

    title = forms.CharField(label='Title', max_length=100)
    parent = forms.ModelChoiceField(queryset=MenuItem.objects.all(),required=False)
    content = forms.ModelChoiceField(queryset=ContentItem.objects.all(),required=False)
    override_url = forms.CharField(label='Override URL', max_length=1000, required=False)
    priority = forms.IntegerField(required=False)
    published = forms.BooleanField(required=False)

    class Meta:
        model = FlatPage
