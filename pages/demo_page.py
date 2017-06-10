
from pages.base_page import Page

class DemoPage(Page):

    def open_page(self):
        self.open_web_page("http://www.google.com")
