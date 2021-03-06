from datetime import datetime

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.search import index
from wagtail.snippets.models import register_snippet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.contrib.routable_page.models import RoutablePageMixin

from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='')
    slug = models.SlugField(default='')
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        FieldPanel('description'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'

class BlogPostTag(TaggedItemBase):
    content_object = ParentalKey('BlogPost', related_name='tagged_items')

class BlogIndexPage(RoutablePageMixin, Page):
    header = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header', classname='full')
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)

        category = request.GET.get('category')

        blogposts = []
        if None != category and '' != category and 'None' != category:
            context['category'] = category
            categoryObj = BlogCategory.objects.get(name=category)
            context['category_description'] = categoryObj.description
            blogposts = self.get_children() \
                .filter(blogpost__categories__name=category)
        else:
            context['category'] = 'All News'
            context['category_description'] = ''
            blogposts =self.get_children()

        blogposts = blogposts.filter(content_type__model= 'blogpost').order_by('-first_published_at')

        paginator = Paginator(blogposts, 15) # Show 5 resources per page
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            resources = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            resources = paginator.page(paginator.num_pages)

            # make the variable 'resources' available on the template
        paged_blogposts = []
        items = []
        count = 0
        for item in resources:
            items.append(item)
            count+=1
            if count % 3 == 0:
                paged_blogposts.append(items)
                items = []

        if items not in paged_blogposts:
            paged_blogposts.append(items)

        context['blogposts'] = paged_blogposts

        return context


class BlogPost(RoutablePageMixin, Page):
    date = models.DateTimeField("Post date", default=datetime.now)
    subtitle = models.CharField(max_length=250, blank=True)
    header_image = models.ForeignKey('wagtailimages.Image',
                                     on_delete=models.SET_NULL, related_name='+', blank=True, null=True, )

    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPostTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('subtitle'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Post meta"),
        FieldPanel('subtitle'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('header_image'),
    ]
