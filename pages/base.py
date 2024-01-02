from playwright.sync_api import Page


class Base:
    def __init__(self, page: Page):
        self.page = page
