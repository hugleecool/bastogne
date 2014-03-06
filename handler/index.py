from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, page=0):
        page = int(page)
        posts = self.db.movie.find().skip(12*page).limit(12)
        self.render('index/index.html', posts=posts, page=page)


class SearchHandler(BaseHandler):
    def get(self):
        self.render('index/search.html')