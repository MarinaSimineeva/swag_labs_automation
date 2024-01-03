from data.consts import Consts
from pages.auth_page import AuthPage


def login_user(browser, username, password):
    browser.goto(Consts.URL)
    page = AuthPage(browser)
    page.pass_auth(username, password)