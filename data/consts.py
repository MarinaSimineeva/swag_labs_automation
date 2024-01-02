class Consts:
    auth_page_title = 'Swag Labs'

    standard_user = {'name': 'standard_user', 'password': 'secret_sauce'}
    visual_user = {'name': 'visual_user', 'password': 'secret_sauce'}
    locked_out_user = {'name': 'locked_out_user', 'password': 'secret_sauce'}
    no_username_user = {'name': '', 'password': 'secret_sauce'}
    wrong_username_user = {'name': 'unknown_user', 'password': 'secret_sauce'}
    no_password_user = {'name': 'standard_user', 'password': ''}
    wrong_password_user = {'name': 'standard_user', 'password': 'unknown_password'}

    error_no_username = 'Epic sadface: Username is required'
    error_no_password = 'Epic sadface: Password is required'
    error_wrong_creds = 'Epic sadface: Username and password do not match any user in this service'
    error_locked_user = 'Epic sadface: Sorry, this user has been locked out.'