import allure
from playwright.sync_api import Page, expect

from data.consts import Consts
from locators.cart_page_locators import CartLocators
from pages.base import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_title = page.locator(CartLocators.cart_title)
        self.cart_badge = page.locator(CartLocators.cart_badge)
        self.cart_icon = page.locator(CartLocators.cart_icon)
        self.remove_item_btn = page.locator(CartLocators.remove_item_btn)
        self.checkout_btn = page.locator(CartLocators.checkout_btn)
        self.continue_shopping_btn = page.locator(CartLocators.continue_shopping_btn)

    def check_cart_screen_contents(self, amount, exp_app_title, exp_continue_shopping_txt, exp_checkout_txt):
        with allure.step(f'Проверяем отображение и текст заголовка : {Consts.app_title}'):
            expect(self.cart_title).to_be_visible(timeout=Consts.Timeout.MEDIUM)
            expect(self.cart_title).to_have_text(exp_app_title)

        with allure.step('Проверяем отображение иконки корзины и бейджа'):
            expect(self.cart_icon).to_be_visible(timeout=Consts.Timeout.MEDIUM)
            if amount:
                expect(self.cart_badge).to_be_visible(timeout=Consts.Timeout.MEDIUM)
                expect(self.cart_badge).to_have_text(str(amount))

        with allure.step(f'Проверяем отображение и текст кнопок {Consts.cart_continue_shopping_btn} и {Consts.cart_checkout_btn}'):
            expect(self.continue_shopping_btn).to_be_visible(timeout=Consts.Timeout.MEDIUM)
            expect(self.continue_shopping_btn).to_have_text(exp_continue_shopping_txt)
            expect(self.checkout_btn).to_be_visible(timeout=Consts.Timeout.MEDIUM)
            expect(self.checkout_btn).to_have_text(exp_checkout_txt)
