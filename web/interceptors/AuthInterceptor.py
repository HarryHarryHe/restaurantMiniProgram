from application import app
from flask import request, redirect, g
from common.models.User import User
from common.libs.user.UserService import UserService
from common.libs.UrlManager import UrlManager
import re
from common.libs.LogService import LogService


@app.before_request  # 装饰器
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path

    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    user_info = check_login()
    g.current_user = None
    if user_info:
        g.current_user = user_info
        app.logger.info(g.current_user.nickname)

    # 加入日志
    LogService.addAccessLog()

    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return

    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return


'''
判断用户是否已经登陆
'''


def check_login():
    cookies = request.cookies
    # 若用户未登陆直接进入主页，则令cookie置为空
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None
    # app.logger.info(auth_cookie)
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    # 登陆有效性的校验 （删除自己的账号退出页面）
    if user_info.status !=1:
        return False

    return user_info
