import tornado.web
from config.config import conf


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def conf(self):
        return conf

    @staticmethod
    def get_side():
        """获取侧边栏内容

        通用侧边栏数据
        """
        side = {
            'tags': '',
        }
        return side

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('public/404.html')
        elif status_code == 500:
            self.render('public/500.html')
        else:
            self.write('error:' + str(status_code))