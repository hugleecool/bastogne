from .base import BaseHandler


class PostHandler(BaseHandler):
    def get(self, pid):
        post = self.db.movie.find_one({'id': int(pid)})
        self.render('post/index.html', post=post)