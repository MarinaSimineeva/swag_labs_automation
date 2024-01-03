import allure
import pytest
from playwright.sync_api import expect

from helpers.login_user import *
from data.consts import Consts
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@allure.story('Корзина')
@pytest.mark.parametrize('amount', [1, None])
def test_cart_screen_contents(browser, amount):
    allure.dynamic.title(f'Отображение экрана корзины: {amount} товаров в корзине')
    login_user(browser, Consts.standard_user['name'], Consts.standard_user['password'])
    if amount:
        inv_page = InventoryPage(browser)
        inv_page.add_item_to_cart()
    cart_page = CartPage(browser)
    cart_page.go_to(Consts.CART_URL)
    cart_page.check_cart_screen_contents(amount)


@allure.story('Корзина')
@allure.title('Удаление товара из корзины')
def test_removing_item_from_cart(browser):
    login_user(browser, Consts.standard_user['name'], Consts.standard_user['password'])
    inv_page = InventoryPage(browser)
    inv_page.add_item_to_cart()
    cart_page = CartPage(browser)
    cart_page.go_to(Consts.CART_URL)
    with allure.step('Удаляем товар из корзины'):
        cart_page.remove_item_btn.click()
    cart_page.check_cart_screen_contents(amount=None)


@allure.story('Корзина')
@allure.title('Навигация на экран списка товаров по клику continue shopping')
def test_nav_to_inventory_screen(browser):
    login_user(browser, Consts.standard_user['name'], Consts.standard_user['password'])
    cart_page = CartPage(browser)
    cart_page.go_to(Consts.CART_URL)
    with allure.step('Нажимаем "Continue shopping"'):
        cart_page.continue_shopping_btn.click()
    with allure.step('Проверяем, что произошел переход на экран списка товаров'):
        expect(browser).to_have_url(Consts.INVENTORY_URL)


@allure.story('Корзина')
@allure.title('Навигация на экран оплаты по клику checkout')
def test_nav_to_checkout(browser):
    login_user(browser, Consts.standard_user['name'], Consts.standard_user['password'])
    cart_page = CartPage(browser)
    cart_page.go_to(Consts.CART_URL)
    with allure.step('Нажимаем Checkout'):
        cart_page.checkout_btn.click()
    with allure.step('Проверяем, что произошел переход на экран оплаты'):
        expect(browser).to_have_url(Consts.CHECKOUT_URL)


@allure.story('Корзина')
@allure.title('Навигация на экран списка товаров  по клику back')
def test_nav_back_to_inventory(browser):
    login_user(browser, Consts.standard_user['name'], Consts.standard_user['password'])
    with allure.step('Переходим на экран корзины'):
        browser.goto(Consts.CART_URL)
    with allure.step('Нажимаем Back'):
        browser.go_back()
    with allure.step('Проверяем, что произошел переход на экран списка товаров'):
        expect(browser).to_have_url(Consts.INVENTORY_URL)
