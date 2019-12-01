SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False

# 解决浏览器看到的中文字符的unicode形式
JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "food"

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]



PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}
MINA_APP = {
    'appid': 'wx45b0f75de4d3f90b',
    'appkey': '1c66bd2b154c999f05280eb6d1f412cf'
}
UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}
APP = {
    'domain': 'http://192.168.237.129:8999'
}
