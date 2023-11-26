handlers=list()
#configure the path
import tornado.web
import tornado.httpserver
from tornado.web import URLSpec


from conf.conf import *
from conf.base import BaseHandler,EnterHandler

from controller.loginC import LoginHandler

handlers=list()

#default address is /
handlers.extend([
    URLSpec("/",EnterHandler,name='enterPoint'),
    URLSpec("/login",LoginHandler,name='loginHandler')
])

#put URL into application
app=tornado.web.Application(handlers=handlers,**setting)