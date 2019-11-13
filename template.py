import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler
from tornado.web import StaticFileHandler
import os

define("port", default=8000, type=int, help="run server on the given port.")


class IndexHandler(RequestHandler):
    def get(self):
        # 模板变量与表达式{{ }}
        house_info = {
            "p1": 198,
            "p2": 200,
            "titles": ["宽窄巷子", "160平大空间", "文化保护区双地铁"],
            "score": 5,
            "comments": 6,
        }
        # 模板控制语句 {% %}
        houses = [
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            },
            {
                "price": 398,
                "title": "宽窄巷子+160平大空间+文化保护区双地铁",
                "score": 5,
                "comments": 6,
                "position": "北京市丰台区六里桥地铁"
            }]
        # houses 为模板的变量名
        self.render("./templates/index.html", houses=houses)
        # self.render("./templates/index.html", **house_info)
        # 函数、转义、块 TODO


if __name__ == "__main__":
    tornado.options.parse_command_line()
    current_path = os.path.dirname(__file__)
    app = tornado.web.Application([
        (r'/', IndexHandler),
        # (r'^/view/(.*)$', StaticFileHandler, {"path": os.path.join(current_path, "statics/html")}),
    ],
        static_path=os.path.join(current_path, "statics"),  # 此参数告诉tornado从哪个位置找静态文件
        templlate_path=os.path.join(current_path, "templates"),  # 此参数告诉tornado从哪个位置找模板文件
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()