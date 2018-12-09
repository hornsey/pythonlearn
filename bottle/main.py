#!/usr/bin/env python
#coding=utf-8

from bottle import route,run,request,view
from bottle import template,static_file
from bottle import error,abort,redirect,default_app
from beaker.middleware import SessionMiddleware

images_path = './images'

@error(404)
def miss(code):
    #错误页面，一般来说，可以在网站制定一个404的HTML页面，然后用return template('404')去访问404这个页面
    return '错误404!\n没找到页面！'

@route('/error')
def nofound():
    #引发404错误
    abort(404)

@route('/page')
def page():
    #当访问/page的时候，跳转到首页
    redirect('/')

@route('/images/<filename:re:.*\.jpeg>')
def server_static(filename):
    return static_file(filename, root=images_path)

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=images_path, download=filename)

@route('/')
def index1():
    return template('index')

@route('/index')
def index():
    return template('index')

@route('/info1')
@view('info')
def info1():
    name = '汪峰子'
    age = '30'
    blog = 'www.wangfeng.com'
    qq = '35218897'
    book = ['python','linux','php']
    price = {'pc':4000,'phone':2000,'bike':600}
    data = {'tname':name, 'tage':age, 'tblog':blog, 'tqq':qq, 'tbook':book,
            'tprice':price, 'tnum':''}
    return data

@route('/info')
def info():
    name = '汪峰'
    age = '30'
    blog = 'www.wangfeng.com'
    qq = '35218897'
    return template('info',tname=name,tage=age,tblog=blog,tqq=qq)
    # id = request.query.id
    # name = request.query.name
    # age = request.query.age
    #
    # return "id=%s,name=%s,age=%s" % (id,name,age)

@route('/login')
def login():
    return template('login')
    #"""
    # <html>
    #     <head>
    #     </head>
    #     <body>
    #     <form action="/login" method="post">
    #     Username:<input name="username" type="text"/>
    #     Password:<input name="password" type="password"/>
    #     <input value="Login" type="submit"/>
    #     </body>
    # </html>
    # """

@route('/login',method='POST')
def do_login():
    """
    post动作登录
    """
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'hornsey' and password == '123456':
        s = request.environ.get('beaker.session')
        s['user'] = username
        s.save
        for k,v in s.items():
            print("K:%s V:%s" % (k, v))
        print("%s save" % s['user'])
    print("%s login" % username)

    return redirect('/')


@route('/hello')
def hello():
    return "Hello www.baidu.com"

@route('/hello/<name>')
def helloName(name):
    return "Hello %s " % name

#设置session参数
session_opts = {
    'session.type':'file',                          # 以文件的方式保存session
    'session.cookei_expires':3600,        # session过期时间为3600秒
    'session.data_dir':'./sessions',  # session存放路径
    'sessioni.auto':True
    }

app = default_app()
app = SessionMiddleware(app, session_opts)
run(app=app,host='0',port=8080,debug=True)


