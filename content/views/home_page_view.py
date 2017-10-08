from django.views import View
from django.shortcuts import render

from content.views.view_utils import get_latest_content, get_menu_items


class HomePage(View):
    """Home page view"""

    def get(self, request):
        # Get the menu
        menu = get_menu_items()

        # Get the latest content for sidebar and footer
        latest_content = get_latest_content()

        # Render the view
        return render(request, "pages/home.html",
                      {"latest_content": latest_content,
                       "menu": menu, })
