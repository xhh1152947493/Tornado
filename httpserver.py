import tornado.web
import tornado.ioloop
import tornado.httpserver


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Get")

    def post(self):
        """对应http的post请求方式"""
        self.write("Hello Post")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # app.listen(8000)
    """
    我们创建了一个HTTP服务器实例http_server，因为服务器要服务于我们刚刚建立的web应用，
    将接收到的客户端请求通过web应用中的路由映射表引导到对应的handler中，
    所以在构建http_server对象的时候需要传出web应用对象app。http_server.listen(8000)将服务器绑定到8000端口。
    """
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    tornado.ioloop.IOLoop.current().start()