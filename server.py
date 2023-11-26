#server startup module
import sys
import tornado.ioloop
import tornado.options

#options is a base class for config the Entire  framework
import tornado.httpserver
from tornado.options import define, options, parse_command_line

#Import all program modules
from application import app

#define the port
define("port", default=8000, help="Server Listen on the given ports", type=int)
#cmd python server.py --help
#cmd python server.py --port=8000 #less than 65535
def main():
    parse_command_line()
    print("Server is running on port %d" % options.port)
    print("stop the server with ctrl+c")
    httpserver = tornado.httpserver.HTTPServer(app)
    #Deploy the server
    httpserver.listen(options.port,reuse_port=False)
    httpserver.start(1)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()