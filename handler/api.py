import json
from .base import BaseHandler


class ApiHandler(BaseHandler):
    def get(self):
        title = self.get_argument('title', '')
        try:
            post = self.db.movie.find_one({'title': title})
            del post['_id']
            self.write(json.dumps(post))
        except TypeError:
            self.write('null')

