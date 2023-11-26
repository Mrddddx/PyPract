#define the core and the base configuration,including debug,adding the security,ect.
import os,pymysql
#define the view floor

setting=dict(
    debug=True,#Allow hot deployment of the program during the development phase
    xsrf_cookies=True,#avoid the hacker attack
    compress_response=True,#default the response compression
    stati_path = os.path.join(os.getcwd(),'static'),#configure the static path
    template_path = os.path.join(os.getcwd(),'templates'),#configure the template path
    cookie_secret='yxxfgjhgjyuut6ytfgyufucjjhfdygfhjfjdghghdhlfyjtdj',#sign up the cookie secret
    static_url_prefix='/static/',#require the static url prefix
    login_url='login',#if the user is not logged in,redirect to the login page
    static_handler_args=dict(default_filename='index.html')
)
#global database operation object
db=pymysql.connect(
    host='localhost',
    user='cnosdb',
    password='cnosdb',
    db='cnosdb',
    autocommit=True
)