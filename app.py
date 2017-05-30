#!/usr/bin/env python
# -*-coding:utf-8-*-
import tornado.web
from tornado.web import URLSpec
import tornado.httpserver
import tornado.options
from tornado.options import define, options
import tornado.ioloop
import settings
from handlers import *

define("port", default=9876, type=int, help="使用端口, --port=9876")


class App(tornado.web.Application):
    def __init__(self):
        handlers = [
            URLSpec(r'/', IndexHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings.settings)

def main():
    tornado.options.parse_command_line()
    app = App()
    server = tornado.httpserver.HTTPServer(app, xheaders=True)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
