# coding:utf-8
from demo import create_app
from demo.modules.home.views import homeRoute
from demo.modules.slaapp.views import slaRoute
from demo.modules.users.views import userRoute
from flask import request

import sys
reload(sys)
sys.setdefaultencoding('utf8')

DEFAULT_MODULES = [
    homeRoute,
    slaRoute,
    userRoute,
]

app = create_app('config.py')

@app.before_request
def before_request():
    """
    这里是全局的方法，在请求开始之前调用。
    其中 flask 有个全局的变量 g，它是和 session 一样的用途，可以使用它来保存当前用户的数据
    Returns:
    """

    # flask多蓝图模板目录冲突解决,参照 http://xuke1668.blog.51cto.com/2129485/1712081
    if request.blueprint is not None:
        bp = app.blueprints[request.blueprint]
        if bp.jinja_loader is not None:
            newsearchpath = bp.jinja_loader.searchpath + app.jinja_loader.searchpath
            app.jinja_loader.searchpath = newsearchpath
        #如果访问非蓝图模块或蓝图中没有指定template_folder,默认使用app注册时指定的全局template_floder.
        else:
            app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]
    else:
            app.jinja_loader.searchpath = app.jinja_loader.searchpath[-1:]

# 注册蓝图
for module in DEFAULT_MODULES:
    app.register_blueprint(module)

