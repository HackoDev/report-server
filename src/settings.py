import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

debug = {
    'debug': True,
    'autoreload': True,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'cookie_secret': 'akdjowifhq8iownrxqiaoxct2go7xiq34bxgq8i37txbtgx87o',
    'user_cookie_key': 'user',
    'template_path': os.path.join(BASE_DIR, 'templates')
}

production = {
    'debug': False,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'cookie_secret': 'mqpun89tcbgo27iuf4nod78quyskeun7423im08129pwI!@()S!(34iw',
    'user_cookie_key': 'user',
    'template_path': os.path.join(BASE_DIR, 'templates')
}
