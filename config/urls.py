from handler import index, post, api


urls = [
    (r'/', index.IndexHandler),
    (r'/page/(\d{0,4})', index.IndexHandler),
    (r'/post/(\d{0,5})', post.PostHandler),
    (r'/search', index.SearchHandler),
    (r'/api/movie', api.ApiHandler),
]
