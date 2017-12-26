#!/usr/bin/env python
import tornado.ioloop
from tornado.options import define, options

from apptication import make_app

define('config', default='debug', help='config file')

if __name__ == '__main__':
    app = make_app(options.config)
    app.listen(8888)
    print("Server running on {port} port".format(port=8888))
    tornado.ioloop.IOLoop.current().start()
