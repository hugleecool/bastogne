import tornado.web
from util.movie import Movie


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def get_douban_movie(self):
        return Movie().get_movie