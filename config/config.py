#数据库配置
database = {
    'host': 'localhost',
    'database': 'notepy',
    'user': 'root',
    'password': 'root',
    'autocommit': True,
    'buffered': True,
}

settings = {
    "app": 'Bastogne',
    "template_path": "templates",
    "static_path": "static",
    "cookie_secret": "entercookiesecret",
    "login_url": "/login",
    "xsrf_cookies": True,
    "debug": False,
}
