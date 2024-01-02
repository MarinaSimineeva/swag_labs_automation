from decouple import config


class Config:
    BROWSER = config('BROWSER')
    HEADLESS = True if config('HEADLESS') == 'true' else False

    URL = 'https://www.saucedemo.com/'
    INVENTORY_URL = 'https://www.saucedemo.com/inventory.html'

