from django.shortcuts import render, redirect
from django.views import View
from content.models import ContentItem, ContentTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from content.view_utils import get_latest_content, layout_selector, get_featured_content


class HomePage(View):
    """Home page view"""

    def get(self, request):
        # get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Render the view
        return render(request, "pages/home.html",
                                            {"latest_content" : latest_content})


class ContentDisplay(View):
    """Single item display"""

    def get(self, request, content_id):
        # query the DB for content by ID
        content = ContentItem.objects.get(pk=content_id)

        # get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Get the latest featured content
        featured_content = get_featured_content()

        # get all tags for sidebar
        tags = ContentTag.objects.all()

        # Set the layout based on the content's layout value
        layout = layout_selector(content.layout.selected)

        # Render the view
        return render(request, layout, {"content" : content,
                                        "latest_content" : latest_content,
                                        "featured_content" : featured_content,
                                        "tags" : tags,})


class ContentDisplayList(View):
    """List recent posts of tag type (default all tags)"""

    def get(self, request, tag=None):
        if tag:
            # If there is a tag, query the database with it
            posts = ContentItem.objects.filter(content_type__selected='post').filter(tags__name=tag).order_by('updated_at')
            title = tag
        else:
            # If there is no tag, query the database for all posts
            posts = ContentItem.objects.filter(content_type__selected='post').order_by('updated_at')
            title = "Recent Posts"

        # Paginate the posts object and show 5 posts per page
        paginator = Paginator(posts, 5)

        # Get the page number from the request url (?page=)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        # Get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Get the latest featured content
        featured_content = get_featured_content()

        # Get the tags that exist in the database
        tags = ContentTag.objects.all()

        # Render the view
        return render(request, "pages/content/content_base.html",
                                                            {"title" : title,
                                                            "posts" : posts,
                                                            "latest_content" : latest_content,
                                                            "featured_content" : featured_content,
                                                            "tags" : tags})
