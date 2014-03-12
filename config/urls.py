from handler import index, movie, api


urls = [
    (r'/', index.MovieHandler),
    (r'/movie', index.MovieHandler),
    (r'/login', index.LoginHandler),
    (r'/logout', index.LogoutHandler),
    (r'/post/(\d{0,5})', movie.PostHandler),
    (r'/post/add', movie.AddHandler),
    (r'/search', index.SearchHandler),
    (r'/api/movie', api.ApiHandler),
]
