# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
from tornado.web import Application
from views.index import MainHandler


class Application(Application):

    def __init__(self):
        handlers = [
            (r'/', MainHandler),
            (r'/(.*)', MainHandler),
        ]
        super(Application, self).__init__(handlers)
