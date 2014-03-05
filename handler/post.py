from .base import BaseHandler
from bson.objectid import ObjectId


class PostHandler(BaseHandler):
    def get(self, pid):
        post = self.db.movie.find_one({'_id': ObjectId(pid)})
        self.render('post/index.html', post=post, douban_movie=self.get_douban_movie(post['title']))