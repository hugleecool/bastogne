from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, page=0):
        page = int(page)
        posts = self.db.movie.find().skip(8*page).limit(8)
        self.render('index/index.html', posts=posts, page=page)