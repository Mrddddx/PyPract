#kun class,and the access settings.With out sign in,return the default page.
from typing import Any
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def write_error(self, status_code: int, **kwargs: Any) -> None:
        print(f"Error{status_code}")
        self.write(f"Error{status_code}")

    def get_current_user(self) -> Any:
        userName=self.get_secure_cookie("userName")
        if isinstance(userName, bytes):
            return userName.decode(encoding="utf-8")
        return None

class EnterHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.redirect("/main")