from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^all/$', views.ContentDisplayList.as_view()),
    url(r'^tag/(?P<tag>.+)$', views.ContentDisplayList.as_view()),
    url(r'^display/(?P<content_id>.+)/$', views.ContentDisplay.as_view()),

    url(r'^content/admin/$', views.ContentAdminHome.as_view()),
    url(r'^content/add/$', views.AddContent.as_view()),
    url(r'^content/edit/(?P<content_id>.+)/$', views.EditContent.as_view()),
    url(r'^content/delete/(?P<content_id>.+)/$', views.DeleteContentItem.as_view()),

    url(r'^content/menu/admin/$', views.MenuAdminHome.as_view()),
    url(r'^content/menu/add/$', views.AddMenuItem.as_view()),
    url(r'^content/menu/edit/(?P<menu_item_id>.+)/$', views.EditMenuItem.as_view()),
    url(r'^content/menu/delete/(?P<menu_item_id>.+)/$', views.DeleteMenuItem.as_view()),
]
