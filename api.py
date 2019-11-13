# RequestHandler类中有很多已经定义的接口函数，我们可以在自己的类中重写这些方法

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(RequestHandler):

    def initialize(self):
        print("调用了initialize()")

    def prepare(self):  # 预处理，即在执行对应请求方式的HTTP方法（如get、post等）前先执行，注意：不论以何种HTTP方式请求，都会执行prepare()方法。
        print("调用了prepare()")

    def set_default_headers(self):
        print("调用了set_default_headers()")

    def write_error(self, status_code, **kwargs):
        print("调用了write_error()")

    def get(self):
        print("调用了get()")

    def post(self):
        print("调用了post()")
        self.send_error(200)  # 注意此出抛出了错误

    def on_finish(self):  # 即在调用HTTP方法后调用。通常该方法用来进行资源清理释放或处理日志等
        print("调用了on_finish()")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    # 路由映射支持正则
    app = tornado.web.Application([
        (r"/", IndexHandler),
        # 两个()，则提取了两个参数，则在对应的处理函数中需要有两个参数接收，当不确定时最好使用不定长参数
        # (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),  # 无名方式
        # (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler),  # 命名方式
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


"""
get:为抛出错误
调用了set_default_headers()
调用了initialize()
调用了prepare()
调用了get()
调用了on_finish()
post:抛出错误
调用了set_default_headers()
调用了initialize()
调用了prepare()
调用了post()
调用了set_default_headers()
调用了write_error()
调用了on_finish()
"""


"""
在正常情况未抛出错误时，调用顺序为：

set_defautl_headers()
initialize()
prepare()
HTTP方法
on_finish()
在有错误抛出时，调用顺序为：

set_default_headers()
initialize()
prepare()
HTTP方法
set_default_headers()
write_error()
on_finish()
"""

"""
HTTP方法
方法	描述
get	请求指定的页面信息，并返回实体主体。
head	类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头
post	向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。
delete	请求服务器删除指定的内容。
patch	请求修改局部数据。
put	从客户端向服务器传送的数据取代指定的文档的内容。
options	返回给定URL支持的所有HTTP方法。
"""