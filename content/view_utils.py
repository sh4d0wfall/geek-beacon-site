from content.models import ContentItem, ContentTag

def get_latest_content():
    """Query the database for the latest content and add it to the array"""

    latest_content = {}
    latest_content['all'] = ContentItem.objects.all().order_by('updated_at')[:4]
    latest_content['ga'] = ContentItem.objects.filter(tags__name='Geeks Abroad').order_by('updated_at')[:4]
    latest_content['gaming'] = ContentItem.objects.filter(tags__name='Gaming').order_by('updated_at')[:4]
    latest_content['osalt'] = ContentItem.objects.filter(tags__name='OS.Alt').order_by('updated_at')[:4]
    latest_content['sqa'] = ContentItem.objects.filter(tags__name='Squirrel Army').order_by('updated_at')[:4]
    
    return latest_content


def layout_selector(layout):
    """Return the HTML file path for the layout supplied"""

    PAGE_LAYOUTS = {'full' : 'pages/home.html',
                   'sidebar' : 'pages/content/content_post.html'}

    return PAGE_LAYOUTS[layout]
