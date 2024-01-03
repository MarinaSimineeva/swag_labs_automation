import allure
from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, screen_url):
        with allure.step(f'Переходим на экран: {screen_url}'):
            self.page.goto(screen_url)
