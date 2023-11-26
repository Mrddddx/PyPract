from conf.base import BaseHandler,EnterHandler
class LoginHandler(BaseHandler):
    def get(self):
        #self.write("default login")
        self.set_header("Content-Type", "text/html; charset=UTF-8")
        self.render("../template/login.html")
