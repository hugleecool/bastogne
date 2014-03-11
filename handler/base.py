import tornado.web
from config.config import conf


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def conf(self):
        return conf

    def get_side(self):
        """获取侧边栏内容

        通用侧边栏数据
        """
        side = {
            'genres': self.db.genres.find(),
            'nav': self.db.genres.find(),
        }
        return side

    def get_same_kind_movie(self, key, post):
        """获取同类影片
        genres 部分匹配，并排除自身
        """
        return self.db.movie.find({key: {'$in': post['genres']}, 'id': {'$ne': post['id']}}).limit(8)

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            self.render('public/404.html')
        elif status_code == 500:
            self.render('public/500.html')
        else:
            self.write('error:' + str(status_code))