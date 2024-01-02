from decouple import config


class Config:
    BROWSER = config('BROWSER')
    HEADLESS = True if config('HEADLESS') == 'true' else False

