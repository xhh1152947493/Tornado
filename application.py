import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import url, RequestHandler

define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(RequestHandler):
    def get(self):
        # 获取url
        python_url = self.reverse_url("python_url")
        # 跳转到127.0.0.1/8000/python
        self.write('<a href="%s">itcast</a>' %
                   python_url)


class ItcastHandler(RequestHandler):
    # 跳转到127.0.0.1/8000/python时，执行初始化函数，执行get()
    def initialize(self, subject):
        self.subject = subject

    def get(self):
        self.write(self.subject)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    # 对于路由中的字典，会传入到对应的RequestHandler的initialize()方法中：
    app = tornado.web.Application([
            (r"/", IndexHandler),
            (r"/cpp", ItcastHandler, {"subject": "c++"}),
            url(r"/python", ItcastHandler, {"subject": "python"}, name="python_url")
        ],
        debug=True)  # debug=True时，tornado会监控源代码，当改动保存时自动重启程序，如果更改有错则会自动退出程序
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()