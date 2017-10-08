from django.http import HttpResponseRedirect
from django.views import View

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from content.forms import AddContentForm
from content.models.content_model import ContentItem, PublishHistory, FeatureHistory
from content.views.view_utils import get_menu_items


"""
  responsible for managing content creation, standard crud view. 

"""
class ContentAdminHome(UserPassesTestMixin, LoginRequiredMixin, View):
    """Content Administrator Home View"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, operation=None):
        menu = get_menu_items()
        content = ContentItem.objects.all()
        return render(request, "pages/content/admin/content_admin.html", {"menu": menu,
                                                                          "content": content})


class AddContent(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Content"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request):
        menu = get_menu_items()
        form = AddContentForm()
        return render(request, "pages/content/admin/add_content.html", {"form": form,
                                                                        "menu": menu})

    def post(self, request):
        form = AddContentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            content = ContentItem()

            content.title = form.cleaned_data['title']
            content.author = form.cleaned_data['author']
            content.header_image = form.cleaned_data['header_image']
            content.thumbnail_image = form.cleaned_data['thumbnail_image']
            content.description = form.cleaned_data['description']
            content.body = form.cleaned_data['body']
            content.category = form.cleaned_data['category']
            content.layout = form.cleaned_data['layout']
            content.content_type = form.cleaned_data['content_type']
            content.save()
            content.tags = form.cleaned_data['tags']
            content.save()

            published = PublishHistory()
            published.content_item = ContentItem.objects.get(id=content.id)
            published.published = form.cleaned_data['published']
            published.save()

            featured = FeatureHistory()
            featured.content_item = ContentItem.objects.get(id=content.id)
            featured.featured = form.cleaned_data['featured']
            featured.image = form.cleaned_data['featured_image']
            featured.save()

            return HttpResponseRedirect('/content/admin/')


class EditContent(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Content"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, content_id=None):

        menu = get_menu_items()
        content = ContentItem.objects.get(pk=content_id)
        try:
            published = PublishHistory.objects.filter(content_item=content_id).order_by('updated_at')
            published = published[0].published
        except:
            published = False
        try:
            result = FeatureHistory.objects.filter(content_item__id=content_id).order_by('updated_at')
            featured = result[0].featured
            featured_image = result[0].image
        except:
            featured = False
            featured_image = None

        form = AddContentForm(initial={'title': content.title,
                                       'description': content.description,
                                       'body': content.body,
                                       'author': content.author,
                                       'category': content.category,
                                       'tags': content.tags.all,
                                       'layout': content.layout,
                                       'content_type': content.content_type,
                                       'published': published,
                                       'featured': featured,
                                       'header_image': content.header_image,
                                       'thumbnail_image': content.thumbnail_image,
                                       'featured_image': featured_image, })

        return render(request, "pages/content/admin/edit_content.html", {"form": form,
                                                                         "menu": menu,
                                                                         "content_id": content_id})

    def post(self, request, content_id=None):
        form = AddContentForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            content, created = ContentItem.objects.get_or_create(id=content_id)

            content.title = form.cleaned_data['title']
            content.header_image = form.cleaned_data['header_image']
            content.thumbnail_image = form.cleaned_data['thumbnail_image']
            content.description = form.cleaned_data['description']
            content.body = form.cleaned_data['body']
            content.author = form.cleaned_data['author']
            content.category = form.cleaned_data['category']
            content.tags = form.cleaned_data['tags']
            content.layout = form.cleaned_data['layout']
            content.content_type = form.cleaned_data['content_type']
            content.save()

            published, created = PublishHistory.objects.get_or_create(content_item__id=content_id,
                                                                      defaults={'published': False,
                                                                                'content_item_id': content_id})
            published.published = form.cleaned_data['published']
            published.save()

            featured, created = FeatureHistory.objects.get_or_create(content_item__id=content_id,
                                                                     defaults={'featured': False,
                                                                               'content_item_id': content_id})
            featured.content_item = ContentItem.objects.get(pk=content_id)
            featured.featured = form.cleaned_data['featured']
            featured.image = form.cleaned_data['featured_image']
            featured.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/content/admin/')


class DeleteContentItem(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Content"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, content_id=None):
        menu = get_menu_items()
        content = ContentItem.objects.get(pk=content_id)
        content.delete()
        return HttpResponseRedirect('/content/admin/')
