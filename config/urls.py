from handler import index, movie, api


urls = [
    (r'/', index.IndexHandler),
    (r'/page/(\d{0,4})', index.IndexHandler),
    (r'/login', index.LoginHandler),
    (r'/logout', index.LogoutHandler),
    (r'/movie', index.MovieHandler),
    (r'/post/(\d{0,5})', movie.PostHandler),
    (r'/post/add', movie.AddHandler),
    (r'/search', index.SearchHandler),
    (r'/api/movie', api.ApiHandler),
]
