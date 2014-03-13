from .base import BaseHandler


class PostHandler(BaseHandler):
    def get(self, pid):
        post = self.db.movie.find_one({'id': int(pid)})
        if post is None:
            self.send_error(404)
        else:
            #每访问一次热度加1
            self.db.movie.update({'id': int(pid)}, {'$inc': {'hot': 1}})
            self.render('post/index.html', post=post, side=self.get_side())


class AddHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('post/add.html', side=self.get_side())

    def post(self, *args, **kwargs):
        pass


class UpdateHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass


class DeleteHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass
