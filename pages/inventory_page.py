import allure
from playwright.sync_api import Page

from pages.base import BasePage
from locators.inventory_page_locators import InventoryLocators


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_to_cart_btn = page.locator(InventoryLocators.add_to_cart_btn)

    def add_item_to_cart(self):
        with allure.step('Добавление в корзину товара: Sauce Labs Backpack'):
            self.add_to_cart_btn.click()
