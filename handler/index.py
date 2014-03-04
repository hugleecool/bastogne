from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        posts = self.db.movie.find().limit(10)
        self.render('index/index.html', posts=posts)