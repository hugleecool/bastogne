from .base import BaseHandler


class PostHandler(BaseHandler):
    def get(self, pid):
        post = self.db.movie.find_one({'id': int(pid)})
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
