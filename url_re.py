import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello itcast.")


class SubjectCityHandler(RequestHandler):
    def get(self, *args):
        self.write(("Subject: %s<br/>City: %s" % (args[0], args[1])))


class SubjectDateHandler(RequestHandler):
    def get(self, **kwargs):
        self.write(("Date: %s<br/>Subject: %s" % (kwargs["subject"], kwargs["date"])))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    # 路由映射支持正则
    app = tornado.web.Application([
        (r"/", IndexHandler),
        # 两个()，则提取了两个参数，则在对应的处理函数中需要有两个参数接收，当不确定时最好使用不定长参数
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),  # 无名方式
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler),  # 命名方式
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()