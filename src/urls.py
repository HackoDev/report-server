import tornado.web
import handlers

url_handlers = [
    tornado.web.URLSpec(r'^/$', handlers.IndexHandler, name='index'),
    tornado.web.URLSpec(r'^/login/$', handlers.LoginHandler, name='login'),
    tornado.web.URLSpec(r'^/logout/$', handlers.LogoutHandler, name='logout'),
    tornado.web.URLSpec(r'^/category/(?P<pk>\d+)/$', handlers.ReportHandler, name='report'),
]
