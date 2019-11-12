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


class UploadHandler(RequestHandler):
    def post(self):
        # 用户上传的文件，为一个字典。
        # 键为上传时的文件名，值为列表可能列表中有多个文件对象，文件对象有三个属性，[文件的实际名字,文件的数据实体，文件的类型]
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            # 获取数据实体
            img_file = img_files[0]["body"]
            # 以二进制打开一个本地文件
            file = open("./save_img", 'wb+')
            # 将图片的数据实体以二进制写入本地文件，实现保存在本地
            file.write(img_file)
            file.close()
        self.write("OK")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


"""
RequestHandler.request 对象存储了关于请求的相关信息，具体属性有：

method HTTP的请求方式，如GET或POST;
host 被请求的主机名；
uri 请求的完整资源标示，包括路径和查询字符串；
path 请求的路径部分；
query 请求的查询字符串部分；
version 使用的HTTP版本；
headers 请求的协议头，是类字典型的对象，支持关键字索引的方式获取特定协议头信息，例如：request.headers["Content-Type"]
body 请求体数据；
remote_ip 客户端的IP地址；
files 用户上传的文件，为字典类型，型如：
{
  "form_filename1":[<tornado.httputil.HTTPFile>, <tornado.httputil.HTTPFile>],
  "form_filename2":[<tornado.httputil.HTTPFile>,],
  ... 
}
tornado.httputil.HTTPFile是接收到的文件对象，它有三个属性：
filename 文件的实际名字，与form_filename1不同，字典中的键名代表的是表单对应项的名字；
body 文件的数据实体；
content_type 文件的类型。 这三个对象属性可以像字典一样支持关键字索引，如request.files["form_filename1"][0]["body"]。
"""