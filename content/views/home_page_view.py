from django.views import View
from django.shortcuts import render

from content.views.view_utils import get_latest_content, get_menu_items


class BasePage(View):
    def refresh(self):
        # # Get the menu
        self.menu = get_menu_items()
        # Get the latest content for sidebar and footer
        self.latest_content = get_latest_content()

class HomePage(BasePage):
    """Home page view"""

    def get(self, request):
        self.refresh()
        # Render the view
        return render(request, "pages/home.html",
                      {
                          "title": "Home",
                          "latest_content": self.latest_content,
                          "menu": self.menu
                      })

class Credits(BasePage):
    """Home page view"""

    def get(self, request):
        self.refresh()
        # Render the view
        return render(request, "pages/credits.html",
                      {
                          "title": "Credits",
                          "latest_content": self.latest_content,
                          "menu": self.menu
                      })
