import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os

define("port", default=8000, type=int, help="run server on the given port.")


# class IndexHandler(RequestHandler):
#     def initialize(self):
#         print("调用了initialize()")
#
#     def prepare(self):  # 预处理，即在执行对应请求方式的HTTP方法（如get、post等）前先执行，注意：不论以何种HTTP方式请求，都会执行prepare()方法。
#         print("调用了prepare()")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
        # http://127.0.0.1:8000/static/html/index.html, 此url也可以访问
        # "path": 提供静态文件的根路径。 "default_filename" 用来指定访问路由中未指明文件名时，默认提供的文件。
        (r'^/()$', StaticFileHandler, {"path": os.path.join(current_path, "statics/html"), "default_filename": "index.html"}),
        # 127.0.0.1:8000/view/index.html，此路径提供了文件名，则在path下寻找index.html文件
        (r'^/view/(.*)$', StaticFileHandler, {"path": os.path.join(current_path, "statics/html")})
    ],
        static_path=os.path.join(current_path, "statics"),  # 此参数告诉tornado从哪个位置找静态文件
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()