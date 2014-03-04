from .base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('hello world')