from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from .models import *

class AddContentForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    header_image = forms.ImageField(required=False)
    thumbnail_image = forms.ImageField(required=False)
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 90, 'rows': 1}),required=False)
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 90, 'rows': 20}),required=False)
    #author = models.ForeignKey(User)
    category = forms.ModelChoiceField(queryset=ContentCategory.objects.all(),required=False)
    tags = forms.ModelMultipleChoiceField(queryset=ContentTag.objects.all(),required=False)
    layout = forms.ModelMultipleChoiceField(queryset=ContentLayout.objects.all())
    content_type = forms.ModelMultipleChoiceField(queryset=ContentType.objects.all())
    published = forms.BooleanField(required=False)
    featured = forms.BooleanField(required=False)

    class Meta:
        model = FlatPage
