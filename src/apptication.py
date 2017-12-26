import jinja2
import tornado.web
import tornado.ioloop
import motor
from tornado_jinja2 import Jinja2Loader

from urls import url_handlers
import settings


def make_app(config: str) -> tornado.web.Application:
    client = motor.MotorClient()
    config_mapper = {'debug': settings.debug,
                     'production': settings.production}
    app_settings = config_mapper.get(config, config_mapper['debug'])
    jinja2_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(app_settings['template_path']),
        autoescape=False
    )
    jinja2_loader = Jinja2Loader(jinja2_env)
    return tornado.web.Application(
        handlers=url_handlers,
        template_loader=jinja2_loader,
        db=client.test,
        **app_settings
    )
