"""配置文件

"""
conf = {
    #分页中每页显示影片数量
    'MOVIE_NUM': 10,
    'RANDOM_MOVIE_NUM': 6,
    #分类中显示的分类数目
    'GENRES_NUM': 100,
    'YEAR': {
        'start': 1930,
        'end': 2014,
    },
    'HOT_MOVIE': {
        #显示数目
        'num': 15,
        #最低点击数目
        'hot': 3,
    }
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
