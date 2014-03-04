from handler import index, post


urls = [
    (r'/', index.IndexHandler),
    (r'/post/(.*)', post.PostHandler),
]
