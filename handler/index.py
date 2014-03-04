from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        posts = self.db.movie.find().limit(5)
        self.render('index/index.html', posts=posts)