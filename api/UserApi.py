# 创建类
import app


class UserLogin:
    # 函数1:验证码获取
    def get_verify_code(self, session):
        return session.get(app.BASE_URL + "index.php?m=Home&c=User&a=verify")

    # 函数2:登录
    def get_login(self, session, username, password, verify_code):
        myData = {"username": username,
                  "password": password,
                  "verify_code": verify_code}
        return session.post(app.BASE_URL + "index.php?m=Home&c=User&a=do_login", data=myData)
