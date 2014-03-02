import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options


class Application(tornado.web.Application):
    def __init__(self):
        handlers = []
        tornado.web.Application.__init__(handlers=handlers)




if __name__ == '__main__':
    tornado.httpserver.HTTPServer
