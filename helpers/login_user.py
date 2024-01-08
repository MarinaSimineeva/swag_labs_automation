from data.consts import Consts
from pages.auth_page import AuthPage


def login_user(browser, username, password):
    page = AuthPage(browser)
    page.go_to(Consts.URL)
    page.pass_auth(username, password)
