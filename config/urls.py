from handler import index, post, api


urls = [
    (r'/', index.IndexHandler),
    (r'/page/(\d{0,4})', index.IndexHandler),
    (r'/post/(.*)', post.PostHandler),
    (r'/api/movie', api.ApiHandler),
]
