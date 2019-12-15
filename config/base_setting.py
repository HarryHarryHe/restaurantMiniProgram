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
    'appid': 'wx8af1207ef4665492',
    'appkey': '2374155613e21f8bf5180ebd9766707a',
    'paykey': '支付密匙',
    'mch_id': '商户账号',
    'callback_url': '/api/order/callback'
}
UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}
APP = {
    'domain': 'http://192.168.237.129:8999'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}
PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价",
}
