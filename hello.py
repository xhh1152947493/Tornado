import tornado.web
import tornado.ioloop

"""
1、创建web应用实例对象，第一个初始化参数为路由映射列表。
2、定义实现路由映射列表中的handler类。
3、创建服务器实例，绑定服务器端口。
4、启动当前线程的IOLoop。
"""


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
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
