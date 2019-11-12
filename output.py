import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(RequestHandler):
    # def get(self):
    #     # write方法是写入到缓冲区的，可以多此追加写入，最终所有缓冲区的内容会一起作为本次请求的响应输出
    #     # self.write("hello itcast 1!</br>")
    #     # self.write("hello itcast 2!</br>")
    #     # self.write("hello itcast 3!</br>")
    #     import json
    #     stu = {
    #         "name": "zzh",
    #         "age": 22,
    #         "gender": 1
    #     }
    #     stu_json = json.dumps(stu)  # 将字典转换成字符串。json.loads将字符串转换成字典
    #     self.write(stu_json)  # 实际上tornado会自动将字典类型转换成json字符串，不过和其他数据一起发送可能会造成格式错误
        # write方法除了帮我们将字典转换为json字符串之外，还帮我们将Content-Type设置为application/json; charset=UTF-8
        # self.set_header("Conten-Type", "application/json;charset=UTF-8") # 利用此方法可以完成write方法所做的工作
        # self.set_status(404)  # 设置状态码
        # self.set_status(404, "there is no page")  # 设置状态码与提示信息
        # self.redirect(r"/sub-city/beijing/first")  # 重新向路由

    # 该方法会在进入HTTP处理方法前先被调用，可以重写此方法来预先设置默认的headers。
    # 注意：在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header。
    def set_default_headers(self):
        print("执行了set_default_headers()")
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为itcast、值为python的header
        self.set_header("itcast", "python")

    def get(self):
        err_code = self.get_argument("code", None)  # 注意返回的是unicode字符串，下同
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(err_code, title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])



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