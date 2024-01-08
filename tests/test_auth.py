import allure
import pytest
from playwright.sync_api import expect
from helpers.login_user import *


@allure.story('Авторизация')
@pytest.mark.positive
@pytest.mark.parametrize('username, password', [(Consts.standard_user['name'], Consts.standard_user['password']),
                                                (Consts.visual_user['name'], Consts.visual_user['password'])])
def test_positive_auth_scenario(browser, username, password):
    allure.dynamic.title(f'Проверяем успешную авторизацию пользователем: {username}')
    login_user(browser, username, password)
    with allure.step('Проверяем переход в каталог после успешной авторизации'):
        expect(browser).to_have_url(Consts.INVENTORY_URL)


@allure.story('Авторизация')
@allure.title('Проверяем, что для заблокированного юзера не проходит авторизация')
@pytest.mark.positive
def test_auth_not_passed_locked_user(browser):
    login_user(browser, Consts.locked_out_user['name'], Consts.locked_out_user['password'])
    auth_page = AuthPage(browser)
    auth_page.check_error_alert(Consts.error_locked_user)
    with allure.step('Проверяем отсутствие перехода в каталог при ошибке авторизации'):
        expect(browser).to_have_url(Consts.URL)


@allure.story('Авторизация')
@allure.title('Проверяем ошибку авторизации без заполнения username, password')
@pytest.mark.negative
def test_auth_not_passed_with_empty_fields(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to(Consts.URL)

    with allure.step('Кликаем "авторизоваться", не заполняя username и password'):
        auth_page.login_btn.click()
    auth_page.check_error_alert(Consts.error_no_username)
    with allure.step('Проверяем отсутствие перехода в каталог при ошибке авторизации'):
        expect(browser).to_have_url(Consts.URL)


@allure.story('Авторизация')
@pytest.mark.negative
@pytest.mark.parametrize('username, password', [(Consts.no_username_user['name'], Consts.no_username_user['password']),
                                                (Consts.wrong_username_user['name'],
                                                 Consts.wrong_username_user['password'])])
def test_auth_not_passed_username_errors(browser, username, password):
    user_str = 'пользователь не заполнил username' if username == '' else 'неверное имя пользователя'
    exp_error = Consts.error_no_username if username == '' else Consts.error_wrong_creds

    allure.dynamic.title(f'Проверяем ошибку авторизации : {user_str}')
    login_user(browser, username, password)
    auth_page = AuthPage(browser)

    auth_page.check_error_alert(exp_error)
    with allure.step('Проверяем отсутствие перехода в каталог при ошибке авторизации'):
        expect(browser).to_have_url(Consts.URL)


@allure.story('Авторизация')
@pytest.mark.negative
@pytest.mark.parametrize('username, password', [(Consts.no_password_user['name'], Consts.no_password_user['password']),
                                                (Consts.wrong_password_user['name'],
                                                 Consts.wrong_password_user['password'])])
def test_auth_not_passed_password_errors(browser, username, password):
    user_str = 'пользователь не заполнил password' if password == '' else 'неверный пароль'
    exp_error = Consts.error_no_password if password == '' else Consts.error_wrong_creds

    allure.dynamic.title(f'Проверяем ошибку авторизации : {user_str}')

    login_user(browser, username, password)
    auth_page = AuthPage(browser)
    auth_page.check_error_alert(exp_error)
    with allure.step('Проверяем отсутствие перехода в каталог при ошибке авторизации'):
        expect(browser).to_have_url(Consts.URL)


@allure.story('Авторизация')
@allure.title('Текст и отображение заголовка экрана авторизации')
@pytest.mark.positive
def test_auth_page_title(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to(Consts.URL)

    with allure.step(f'Проверяем отображение и текст заголовка экрана авторизации: {Consts.auth_page_title}'):
        expect(auth_page.auth_title).to_be_visible(timeout=Consts.Timeout.SMALL)
        expect(auth_page.auth_title).to_have_text(Consts.auth_page_title)
