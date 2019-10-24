import hashlib, base64, random, string


class UserService():

    @staticmethod
    def geneAuthCode(user_info):
        m = hashlib.md5()
        str = "%s-%s-%s-%s" % (user_info.uid, user_info.login_name, user_info.login_pwd, user_info.login_salt)
        m.update(str.encode("utf8"))
        return m.hexdigest()

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        # 因为hashlib是对二进制进行加密的，如果直接对字符串加密的话， 会报错的。因此需要通过encode将字符串转码成二进制格式。
        str = "%s-%s" % (base64.encodebytes(pwd.encode("utf8")), salt)
        m.update(str.encode("utf8"))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return "".join(keylist)
