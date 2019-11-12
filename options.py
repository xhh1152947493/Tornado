import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config

# type，从命令行或配置文件导入参数的时候tornado会根据这个类型转换输入的值
tornado.options.define("port", default=8000, type=int, help="run server on the given port.")  # 定义服务器监听端口选项
tornado.options.define("hello_world", default=[], type=str, multiple=True, help="test.")  # 无意义，演示多值情况


class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Get")

    def post(self):
        """对应http的post请求方式"""
        self.write("Hello Post")


if __name__ == "__main__":
    # python3 options.py --port=9000 --hello_world=python,c++,java,php,ios
    # tornado.options.parse_command_line()  # 转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。
    # 追加命令行参数的方式是--myoption=myvalue
    # 从配置文件导入option
    # tornado.options.parse_config_file("./config")
    print(tornado.options.options.hello_world)  # tornado.options.options全局的options对象，所有定义的选项变量都会作为该对象的属性。
    print(tornado.options.options.port)  # tornado.options.options全局的options对象，所有定义的选项变量都会作为该对象的属性。
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
