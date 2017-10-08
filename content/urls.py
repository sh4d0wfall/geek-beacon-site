from django.conf.urls import url

from content.views import content_view, menu_view, home_page_view, content_display_view

urlpatterns = [
    url(r'^$', home_page_view.HomePage.as_view(), name='home'),
    url(r'^all/$', content_display_view.ContentDisplayList.as_view()),
    url(r'^tag/(?P<tag>.+)$', content_display_view.ContentDisplayList.as_view()),
    url(r'^display/(?P<content_id>.+)/$', content_display_view.ContentDisplay.as_view()),

    url(r'^content/admin/?$', content_view.ContentAdminHome.as_view()),
    url(r'^content/add/?$', content_view.AddContent.as_view()),
    url(r'^content/edit/(?P<content_id>.+)/$', content_view.EditContent.as_view()),
    url(r'^content/delete/(?P<content_id>.+)/$', content_view.DeleteContentItem.as_view()),

    url(r'^content/menu/admin/?$', menu_view.MenuAdminHome.as_view()),
    url(r'^content/menu/add/?$', menu_view.AddMenuItem.as_view()),
    url(r'^content/menu/edit/(?P<menu_item_id>.+)/$', menu_view.EditMenuItem.as_view()),
    url(r'^content/menu/delete/(?P<menu_item_id>.+)/$', menu_view.DeleteMenuItem.as_view()),
]
