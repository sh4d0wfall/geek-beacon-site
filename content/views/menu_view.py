from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from django.views import View

from content.forms import AddMenuItemForm
from content.models.menu_model import MenuItem
from content.views.view_utils import get_menu_items


class MenuAdminHome(UserPassesTestMixin, LoginRequiredMixin, View):
    """Menu Administrator Home View"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, operation=None):
        menu = get_menu_items()
        content = MenuItem.objects.all()
        return render(request, "pages/content/admin/menu/menu_admin.html", {"menu": menu,
                                                                            "content": content})


class AddMenuItem(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Menu Items"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, operation=None):
        menu = get_menu_items()
        form = AddMenuItemForm()
        return render(request, "pages/content/admin/menu/menu_item_add.html", {"form": form,
                                                                               "menu": menu})

    def post(self, request, operation=None):
        form = AddMenuItemForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            menu_item = MenuItem()

            menu_item.parent = form.cleaned_data['parent']
            menu_item.content = form.cleaned_data['content']
            menu_item.title = form.cleaned_data['title']
            menu_item.override_url = form.cleaned_data['override_url']
            menu_item.priority = form.cleaned_data['priority']
            menu_item.published = form.cleaned_data['published']

            menu_item.save()

            return HttpResponseRedirect('/content/menu/admin/')


class EditMenuItem(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Menu Items"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, menu_item_id=None):

        menu = get_menu_items()

        content = MenuItem.objects.get(pk=menu_item_id)

        form = AddMenuItemForm(initial={'title': content.title,
                                        'content': content.content,
                                        'parent': content.parent,
                                        'override_url': content.override_url,
                                        'priority': content.priority,
                                        'published': content.published,
                                        })

        return render(request, "pages/content/admin/menu/menu_item_edit.html", {"form": form,
                                                                                "menu": menu,
                                                                                "menu_item_id": menu_item_id})

    def post(self, request, menu_item_id=None):
        form = AddMenuItemForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            try:
                menu_item = MenuItem(pk=menu_item_id)
            except Exception as e:
                print(e)

            menu_item.parent = form.cleaned_data['parent']
            menu_item.content = form.cleaned_data['content']
            menu_item.title = form.cleaned_data['title']
            menu_item.override_url = form.cleaned_data['override_url']
            menu_item.priority = form.cleaned_data['priority']
            menu_item.published = form.cleaned_data['published']

            menu_item.save()

            return HttpResponseRedirect('/content/menu/admin/')


class DeleteMenuItem(UserPassesTestMixin, LoginRequiredMixin, View):
    """View to Add Content"""

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Editor', ])

    def get(self, request, menu_item_id=None):
        menu = get_menu_items()
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        menu_item.delete()
        return HttpResponseRedirect('/content/menu/admin/')
