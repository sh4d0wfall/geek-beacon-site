from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.HomePage.as_view()),
    url(r'^all/$', views.ContentDisplayList.as_view()),
    url(r'^tag/(?P<tag>.+)$', views.ContentDisplayList.as_view()),
    url(r'^display/(?P<content_id>.+)/$', views.ContentDisplay.as_view()),
    url(r'^content/admin/$', views.ContentAdmin.as_view()),
]
