import pytest
from playwright.sync_api import expect
from data.config import Config
from pages.auth_page import AuthPage
from data.consts import Consts


@pytest.mark.positive
def test_auth_page_title(browser):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    expect(auth_page.auth_title).to_be_visible(visible=True, timeout=12000)
    expect(auth_page.auth_title).to_have_text(Consts.auth_page_title)


@pytest.mark.positive
@pytest.mark.parametrize('username, password', [(Consts.standard_user['name'], Consts.standard_user['password']),
                                                (Consts.visual_user['name'], Consts.visual_user['password'])])
def test_positive_auth_scenario(browser, username, password):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    auth_page.pass_auth(username, password)
    expect(browser).to_have_url(Config.INVENTORY_URL)


@pytest.mark.positive
def test_auth_not_passed_locked_user(browser):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    auth_page.pass_auth(Consts.locked_out_user['name'], Consts.locked_out_user['password'])
    auth_page.check_error_alert(Consts.error_locked_user)
    expect(browser).to_have_url(Config.URL)


@pytest.mark.negative
def test_auth_not_passed_with_empty_fields(browser):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    auth_page.login_btn.click()
    auth_page.check_error_alert(Consts.error_no_username)
    expect(browser).to_have_url(Config.URL)


@pytest.mark.negative
@pytest.mark.parametrize('username, password', [(Consts.no_username_user['name'], Consts.no_username_user['password']),
                                                (Consts.wrong_username_user['name'],
                                                 Consts.wrong_username_user['password'])])
def test_auth_not_passed_username_errors(browser, username, password):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    auth_page.pass_auth(username, password)
    if username == Consts.no_username_user['name']:
        auth_page.check_error_alert(Consts.error_no_username)
    else:
        auth_page.check_error_alert(Consts.error_wrong_creds)
    expect(browser).to_have_url(Config.URL)


@pytest.mark.negative
@pytest.mark.parametrize('username, password', [(Consts.no_password_user['name'], Consts.no_password_user['password']),
                                                (Consts.wrong_password_user['name'],
                                                 Consts.wrong_password_user['password'])])
def test_auth_not_passed_password_errors(browser, username, password):
    browser.goto(Config.URL)
    auth_page = AuthPage(browser)

    auth_page.pass_auth(username, password)
    if password == Consts.no_password_user['password']:
        auth_page.check_error_alert(Consts.error_no_password)
    else:
        auth_page.check_error_alert(Consts.error_wrong_creds)
    expect(browser).to_have_url(Config.URL)
