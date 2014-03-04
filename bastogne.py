import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import define, options
from pymongo import MongoClient
from config.config import settings
from config.urls import urls as handlers


define('port', default=10000, help='监听端口', type=int)
handlers.append((r"(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])))


class Application(tornado.web.Application):
    def __init__(self):
        client = MongoClient()
        self.db = client.bastogne
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(Application())
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()