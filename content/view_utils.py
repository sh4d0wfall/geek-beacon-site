from content.models import MenuItem, ContentItem, ContentTag, FeatureHistory

def get_menu_items():
    """Query the database for the current menu items and organize them"""

    menu = {}
    submenu = {}

    # Query the database for published menu items with no parent (main menu items)
    menu['main'] = MenuItem.objects.filter(published=True).filter(parent__isnull=True).order_by('priority')

    # Query the database for published menu items with a parent of a main menu item.
    # Then do the same for those sub-menu items and put it all into a big dict
    # This gives us a main menu with a 2 level deep sub-menu
    for parent in menu['main']:
        menu[parent.title] = MenuItem.objects.filter(published=True).filter(parent__title__exact=parent.title).order_by('priority')
        for subitem in menu[parent.title]:
            menu[subitem] = MenuItem.objects.filter(published=True).filter(parent__title__exact=subitem).order_by('priority')

    return menu



def get_latest_content():
    """Query the database for the latest content and add it to the array"""

    latest_content = {}
    latest_content['all'] = ContentItem.objects.all().order_by('updated_at')[:4]
    latest_content['ga'] = ContentItem.objects.filter(tags__name='Geeks Abroad').order_by('updated_at')[:4]
    latest_content['gaming'] = ContentItem.objects.filter(tags__name='Gaming').order_by('updated_at')[:4]
    latest_content['osalt'] = ContentItem.objects.filter(tags__name='OS.Alt').order_by('updated_at')[:4]
    latest_content['sqa'] = ContentItem.objects.filter(tags__name='Squirrel Army').order_by('updated_at')[:4]

    return latest_content


def get_featured_content():
    """Query the database for the latest featured content and add it to the array"""

    return FeatureHistory.objects.filter(featured=True).order_by('updated_at')[:3]


def layout_selector(layout):
    """Return the HTML file path for the layout supplied"""

    # This dictionary could probably be moved, not sure where to, just saying.
    PAGE_LAYOUTS = {'sidebar' : 'pages/content/content_post.html',}

    return PAGE_LAYOUTS[layout]
